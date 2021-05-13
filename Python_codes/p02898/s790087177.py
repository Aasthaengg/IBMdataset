N,K = map(int,input().split())
h = list(map(int,input().split()))
h = sorted(h)

line = 0
bool1 = False
for i in range(N):
  if h[i] >= K:
    line = i
    bool1 = True
    break

if bool1:
  print(N-i)
else:
  print(0)