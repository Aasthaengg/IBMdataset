def li():
    return list(map(int, input().split()))


def mi():
    return map(int, input().split())


N = int(input())
K = int(input())
x = li()

res = 0

for i in range(len(x)):
    res += min(x[i], K - x[i]) * 2

print(res)
