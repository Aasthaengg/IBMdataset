N = int(input())
A = list(map(int, input().split()))

ans = 10 ** 16
cnt = 0
for A in A:
    while A % 2 == 0:
        A = int(A / 2)
        cnt += 1
    ans = min(cnt, ans)
    cnt = 0

print(ans)

