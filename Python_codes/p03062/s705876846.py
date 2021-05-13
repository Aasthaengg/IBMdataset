N = int(input())
A = list(map(int, input().split()))

Flag = False
cnt = 0
S = 0
m = 10**9

for i in A:
  if i == 0:
    Flag = True
  elif i > 0:
    S += i
    m = min(m, i)
  else:
    S += -i
    cnt ^= 1
    m = min(m, -i)

if Flag or cnt == 0:
  print(S)
else:
  print(S-2*m)