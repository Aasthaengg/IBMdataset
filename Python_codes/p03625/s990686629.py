N=int(input())
S=list(map(int,input().split()))
S.sort()
S.reverse()

dic={}
for i in range(N):
    tmp=S[i]
    if tmp in dic:
        dic[tmp]+=1
    else:    
        dic[tmp]=1
kouho1=0
keys = [k for k, v in dic.items() if v >= 4]
keys.sort()
keys.reverse()
if len(keys)>=1:
    kouho1=keys[0]*keys[0]

kouho2=0
keys = [k for k, v in dic.items() if v >= 2]
keys.sort()
keys.reverse()
if len(keys)>=2:
    kouho2=keys[0]*keys[1]

print(max(kouho1,kouho2))


