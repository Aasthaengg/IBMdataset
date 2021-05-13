N,Q = map(int,input().split())
S = input()
total = [0]*N

for i in range(1,N):
  if S[i] =="C" and S[i-1] == "A":
    total[i] = total[i-1] + 1
  else:
    total[i] = total[i-1]
for i in range(Q):
  r,l = map(int,input().split())
  print(total[l-1] -total[r-1])