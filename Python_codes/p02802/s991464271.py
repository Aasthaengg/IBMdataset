N,M = map(int,input().split())

acli = [0]*N
wali = [0]*N

for _ in range(M):
  P,S = map(str,input().split())
  P = int(P)-1
  if acli[P] == 1:
    continue
  if S == "AC":
    acli[P] = 1
  else:
    wali[P] += 1
    
for i in range(N):
  if acli[i] == 0:
    wali[i] = 0
    
print(sum(acli),sum(wali))