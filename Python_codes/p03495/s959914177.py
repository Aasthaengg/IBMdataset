from collections import Counter

N,K=map(int,input().split())
A=list(map(int,input().split()))

c = Counter(A)
val = sorted(c.values())

if len(val) <= K:
  print(0)
  exit()
  
print(sum(val[:len(val)-K]))