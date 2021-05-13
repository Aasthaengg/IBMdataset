from sys import stdin

N = int(stdin.readline())

result = {}


def comb(n, r):
    up = 1
    down = 1
    for i in range(r):
        up *= n - i
        down *= i + 1
    return up // down


for _ in range(N):
    text = ''.join(sorted(stdin.readline().rstrip()))

    if text in result:
        result[text] += 1
    else:
        result[text] = 1

answer = 0
for v in result.values():
    answer += comb(v, 2)

print(answer)
