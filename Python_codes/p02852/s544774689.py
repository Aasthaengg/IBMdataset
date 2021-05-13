from collections import deque
N,M=map(int,input().split())
S=list(input()) #S[0]....S[N]
flag=1
done=0
piv=N
ans=deque()
while flag==1:
    done=0
    for i in range(max(0,piv-M),piv):
        if S[i]=="0":
            ans.appendleft(piv-i)
            piv=i
            done=1
            break
    if piv==0:
        break
    if done==0:
        flag=0
        break
    #print(piv,ans)
#print(flag)
if flag==1:
    print(*ans)
else:
    print("-1")