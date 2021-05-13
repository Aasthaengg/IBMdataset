N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
last_dish = 0
a = 0
b = 0
c= 0
manzoku = 0
for i in range(N):
  a = A[i]
  manzoku += B[i]
  if last_dish != 0 and last_dish + 1 == A[i]:
    manzoku += C[last_dish - 1]
  last_dish = A[i]
print(manzoku)