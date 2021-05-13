from collections import Counter 
n=int(input())
a=Counter([int(input()) for _ in range(n)])
ans=0
for i in a.values():
  ans+=i%2
print(ans)