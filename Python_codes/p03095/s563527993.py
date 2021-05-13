from collections import Counter
N=int(input())
S=input()
ans=1
s=Counter(S)
for key,value in s.items():
    ans*=value+1
print((ans-1)%(10**9+7))