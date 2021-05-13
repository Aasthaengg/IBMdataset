n=int(input())
a_num=0
b_num=0
set_num=0
ans=0
for i in range(n):
    s=list(input())
    for j in range(len(s)-1):
        if s[j]+s[j+1]=="AB":
            ans+=1
    if s[0]=="B" and s[-1]=="A":
        set_num+=1
    elif s[0]=="B":
        b_num+=1
    elif s[-1]=="A":
        a_num+=1
if set_num==0:
    print(ans+min(a_num,b_num))
else:
    ans+=set_num-1
    if not(a_num==0 and b_num==0):
        a_num+=1
        b_num+=1
    print(ans+min(a_num,b_num))