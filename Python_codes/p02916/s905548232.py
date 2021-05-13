n = int(input())
A = list(map(int,input().split())) + [0]
B = list(map(int,input().split()))
C = [0] + list(map(int,input().split()))

ans = sum(B)
for i in range(n):
  if A[i]+1 == A[i+1]:
    ans += C[A[i]]
print(ans)

