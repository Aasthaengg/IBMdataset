N = int(input())
A = list(map(int, input().split()))
B = [0] * (10**5+1)
for a in A:
    B[a] += 1
ans = 0
for b in B:
    if b > 1:
        ans += b - 1
if ans & 1:
    ans += 1
print(N - ans)