N = int(input())
A = list(map(int, input().split()))
A = [A[n]-n for n in range(N)]
A.sort()
if N % 2 == 1:
  A = [abs(a - A[N//2]) for a in A]
  ans = sum(A)
else:
  temp = A
  A = [abs(a - A[N//2]) for a in A]
  ans = sum(A)
  A = [abs(a - temp[N//2-1]) for a in temp]
  ans = min(ans, sum(A))

print(ans)