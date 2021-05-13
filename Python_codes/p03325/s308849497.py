N = int(input())
alist = list(map(int, input().split()))

ans = 0


def canDiv(val):
    cnt = 0
    while True:
        if val % 2 == 0:
            cnt += 1
            val //= 2
        else:
            return cnt


for a in alist:
    ans += canDiv(a)

print(ans)
