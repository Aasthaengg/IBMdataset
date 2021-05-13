from collections import Counter
n=int(input())
L=[int(input()) for i in range(n)]
L1=Counter(L)
ans=0
for i in L1:
    if L1[i]%2!=0:
        ans+=1
print(ans)