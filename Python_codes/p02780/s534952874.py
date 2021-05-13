N, K = map(int, input().split())

P = list(map(int, input().split()))


def CalculateExpectedValu(n):
    bunbo = 1 / n
    ans = 0

    for i in range(1,n+1):
        ans = ans + (i*bunbo)

    return ans

number = 0
CumulativeSum = [0]

for i in P:
    number = number + CalculateExpectedValu(i)
    CumulativeSum.append(number)

ans = 0



for i in range(0 , (len(CumulativeSum)-K)):
    tmpans = CumulativeSum[i+K] - CumulativeSum[i]
    ans = max(ans, tmpans)

print(ans)
