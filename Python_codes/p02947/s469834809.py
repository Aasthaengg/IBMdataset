from collections import Counter
n=int(input())
s=[]
for _ in range(n):
  s.append(''.join(sorted([i for i in input()])))
s=Counter(s)
ans=0
for i in Counter(s).values():
  ans+=i*(i-1)//2
print(ans)