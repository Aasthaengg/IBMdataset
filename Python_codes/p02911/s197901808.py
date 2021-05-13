n,k,q=list(map(int,input().split()))
li=[k for _ in range(n)]

for _ in range(q):
  a=int(input())
  li[a-1] += 1
  
li=[l-q for l in li]

for l in li:
  print("No") if l <= 0 else print("Yes")