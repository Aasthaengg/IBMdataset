n = int(input())
a = list(map(int, input().split()))

cnt = 1
for e in a:
    if e % 2 == 0:
        cnt *= 2

ans = 3 ** n - cnt
print(ans)
