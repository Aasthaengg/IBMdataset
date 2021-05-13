N = int(input())
A = sorted(list(map(int,input().split())))
mod = 10**9 + 7
B = []
if N % 2 == 0:
  for i in range(1, N//2 + 1):
    B.append(i*2 - 1)
    B.append(i*2 - 1)
else:
  for i in range(1, N//2 + 1):
    B.append(i*2)
    B.append(i*2)
  B.append(0)
B.sort()

if A != B:
  print(0)
else:
  if N % 2 == 0:
    print(pow(2, N//2, mod))
  else:
    print(pow(2, (N-1)//2, mod))