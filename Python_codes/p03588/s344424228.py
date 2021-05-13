n = int(input())
ab = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    ab[i] = (a, b)
ab.sort()

ans = ab[n-1][0] - ab[0][0] + 1
ans += ab[0][0]-1
ans += ab[n-1][1]
print(ans)