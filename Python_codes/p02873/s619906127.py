S = list(map(str,input()))
# s = "><<<<><<"
# S = list(map(str,s))
num = [-1]*(len(S)+1)
index0 = list()
than = 0# 0 == >, 1 == <
#----------------------------------------
for i in range(len(S)):
    if(S[i] == '<'):
        if(than == 0):
            num[i] = 0
            index0.append(i)
        than = 1
    else:
        than = 0
if(S[-1] == '>'):
    num[-1] = 0
    index0.append(len(S)+1)
#--------------------------------------
if(index0[0] == 0):
    i = 1
    while(True):
        num[i] = num[i-1]+1
        if(i >= len(S)):break
        if(S[i] == '>'):
            break
        i+=1
    index0.pop(0)
if(len(index0)>0):
    if(index0[-1] == len(S)+1):
        i = len(S)-1
        while(True):
            num[i] = num[i+1]+1
            i-=1
            if(i < 0):break
            if(S[i] == '<'):break
        index0.pop(-1)

while(len(index0)>0):
        for i in reversed(range(0,index0[0])):
            if(S[i] == '<'):
                break
            num[i] = max(num[i],num[i+1]+1)
        for i in range(index0[0]+1,len(S)+1):
            num[i] = max(num[i],num[i-1]+1)
            if(i >= len(S)):break
            if(S[i]== '>'):break
        index0.pop(0)

ans = 0
for i in range(len(num)):
    ans += num[i]
print(ans)
