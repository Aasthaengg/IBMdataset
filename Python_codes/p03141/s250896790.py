N = int(input())
A, B = [], []
for i in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)
  
l = []
for i in range(N):
  l.append(A[i]+B[i])
l.sort(reverse=True)

ans = 0
for i in range(N//2):
  ans += l[2*i]
if N % 2 == 1:
  ans += l[-1]
ans -= sum(B)
print(ans)