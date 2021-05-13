import math

def resolve():

    n = int(input())
    values = list(map(int, input().split(' ')))

    values.sort(reverse=True)

    ans = 0

    for i in range(1, n):

        ans += values[math.floor(i / 2)]

    print(ans)


resolve()
