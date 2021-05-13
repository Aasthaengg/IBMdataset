N = int(input())
A = list(map(int,input().split()))
Q = int(input())
s = sum(A)
K = [0] *(100000 + 1)
for i in A:
  K[i] += 1
for i in range(Q):
  B , C = map(int,input().split())
  s += (C - B) * K[B]
  K[C] += K[B]
  K[B] = 0
  print(s)