N = int(input())
K = int(input())
sumDis = 0
if N == 1:
    x = int(input())
    disA = x * 2
    disB = (K - x) * 2
    sumDis += min(disA, disB)
else:
    x = list(map(int, input().split()))
    for i in range(N):
        disA = x[i] * 2
        disB = (K - x[i]) * 2
        sumDis += min(disA, disB)
print(sumDis)