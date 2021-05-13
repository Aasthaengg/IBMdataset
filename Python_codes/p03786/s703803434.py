import itertools
N = int(input())
A = list(map(int, input().split()))
A.sort()
AA = list(itertools.accumulate(A))
for i in range(N-1):
  if AA[N-2-i]*2 < A[N-1-i]:
    print(i+1)
    exit()
print(N)