from sys import stdin
N = int(stdin.readline().rstrip())
A = [int(_) for _ in stdin.readline().rstrip().split()]
ans = 0
for i in range(N):
    if (i+1) % 2 == 1 and A[i] % 2 == 1:
        ans += 1
print(ans)