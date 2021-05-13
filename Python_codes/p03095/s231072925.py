from collections import Counter
n=int(input())
s=input()
S=Counter(s)

ans=1
for i in S.values():
    ans *=i+1
print((ans-1)%(10**9+7))