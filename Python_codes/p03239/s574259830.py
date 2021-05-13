N,T = map(int,input().split())
CT = []
for n in range(N):
  c,t = map(int,input().split())
  CT.append([c,t])
CT = sorted(CT,key=lambda x: x[0])
ans = True
for ct in CT:
  if ct[1] <= T:
    print(ct[0])
    ans = False
    break
if ans:
  print("TLE") 
