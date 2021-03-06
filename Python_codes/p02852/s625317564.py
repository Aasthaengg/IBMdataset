import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, M = lr()
S = sr()
# マスNからスタート
cur = N
answer = []
while cur > 0:
    for x in range(M, 0, -1):
        if cur - x < 0 or S[cur - x] == '1':
            continue
        answer.append(x)
        cur -= x
        break
    else:
        print(-1)
        exit()

answer = answer[::-1]
print(*answer)
# 53