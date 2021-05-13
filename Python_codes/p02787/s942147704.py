import math

H,N = map(int,input().split())
ARR = [list(map(int,input().split())) for i in range(N)]
def calculate(h, n, arr):

    brr = [math.inf] * (h + 1)

    brr[0] = 0
    for i in range(h + 1):
        for j in range(n):
            damage = arr[j][0]
            cost = arr[j][1]

            nextDamage = i + damage

            if nextDamage > h:
                nextDamage = h

            nextCost = min(brr[nextDamage], brr[i] + cost)
            brr[nextDamage] = nextCost

    print(brr[-1])

calculate(H, N, ARR)
