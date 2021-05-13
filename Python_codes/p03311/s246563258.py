N = int(input())
A = list(map(int,input().split()))
for i in range(N):
  A[i] -= i+1
A.sort()
#print(A)

def calc(b):
  res = 0
  for i in range(N):
    res += abs(A[i]-b)
  return res

if N % 2 == 1:
  print(calc(A[N//2]))
else:
  print(min(calc(A[N//2]),calc(A[(N-1)//2])))
