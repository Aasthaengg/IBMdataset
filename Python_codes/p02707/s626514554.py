N = int(input())
A = [int(x) for x in input().split()]
ans = [0 for i in range(N)]
for i in range(0,N-1):
  ans[A[i]-1] += 1
print(*ans, sep='\n')