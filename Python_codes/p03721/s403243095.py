N,K=map(int,input().split())
AB=sorted([list(map(int,input().split()))for i in range(N)])

c=0
for ab in AB:
  c+=ab[1]
  if c>=K:
    exit(print(ab[0]))