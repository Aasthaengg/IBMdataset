n = int(input())
A = [0] * n
B = [0] * n
ans = 0
mod = 0
for i in range(n):
    A[i], B[i] = map(int, input().split())

for i in range(n-1, -1, -1):
    ans += 0 if (A[i]+ans)%B[i]==0 else B[i] - (A[i]+ans)%B[i]
print(ans)