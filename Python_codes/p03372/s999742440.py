N, C = map(int, input().split())
INF = 10**20
rightSushi = [tuple(map(int, input().split())) for _ in range(N)]
leftSushi = [(C - x, v) for x, v in rightSushi[:: -1]]

def calc(sushi):
    ret = [-INF] * (N + 1)
    ret[0] = 0
    vSum = 0
    for i, (x, v) in enumerate(sushi, start=1):
        vSum += v
        ret[i] = max(vSum - x, ret[i - 1])
    return ret

leftV = calc(leftSushi)
rightV = calc(rightSushi)

ans = 0
vSum = 0
for right, (x, v) in enumerate(rightSushi, start=1):
    vSum += v
    ans = max(
        ans,
        vSum - x,
        vSum - x * 2 + leftV[N - right]
    )

vSum = 0
for left, (x, v) in enumerate(leftSushi, start=1):
    vSum += v
    ans = max(
        ans,
        vSum - x,
        vSum - x * 2 + rightV[N - left]
    )

print(ans)