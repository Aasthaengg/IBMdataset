N = int(input())
A = list(map(int, input().split()))

ans = 0
even = [a % 2 == 0 for a in A]
for i in range(2 ** N):
    tmp = even.copy()
    cnt = 0
    for j in range(N):
        if ((i >> j) & 1):
            tmp[j] = not tmp[j]
            cnt += 1
    if sum(tmp) > 0:
        ans += 2 ** cnt if i != 0 else 1

print(ans)
