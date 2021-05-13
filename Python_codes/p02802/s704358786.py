N,M=map(int,input().split())
wa=[0]*N
pen=[0]*N
ac=[0]*N
for x in range(M):
  P,S=input().split()
  if S=="WA" and ac[int(P)-1]==0:
    wa[int(P)-1] += 1
  elif S=="AC" and ac[int(P)-1]==0:
    ac[int(P)-1] += 1
    pen[int(P)-1] = wa[int(P)-1]
print(f"{sum(ac)} {sum(pen)}")