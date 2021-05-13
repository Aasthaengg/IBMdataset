N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
s = 0

A = sorted(A)
B = sorted(B)
C = sorted(C)

ia = -1
ic = -1

for b in B:
  while True:
    if ia == N-1 or A[ia+1]>=b: 
      break
    ia += 1
  while True:
    if ic == N-1 or C[ic+1]>b:
      break
    ic += 1
  s += (ia+1)*(N-ic-1)
    
print(s)