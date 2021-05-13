max = 0
a = [0]
N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))
while True:
  if N == 1:
    print("0")
    break
  for i in range(N):
    if V[i] > C[i]:
      a.append(V[i]-C[i])
  for i in a:
    max += i
  print(max)
  break