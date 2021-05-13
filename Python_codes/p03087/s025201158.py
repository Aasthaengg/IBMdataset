N,Q = map(int,input().split())
S = input()
ruisekiwa = [0]*(N+1)
mode = 0
now = 0
for i in range(N):
  if S[i:i+2] == "AC":
    now += 1
  ruisekiwa[i+1] = now
for i in range(Q):
  l,r = map(int,input().split())
  print(ruisekiwa[r-1]-ruisekiwa[l-1])