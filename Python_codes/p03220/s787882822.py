N = int(input())
T,A = list(map(int,input().split()))
H = list(map(int,input().split()))
idealH = (T - A) * 1000 / 6
minDeltaHeight = 10000000
minIndex = 0
for i in range(N):
    deltaHight = abs(idealH - H[i])

    if minDeltaHeight > deltaHight:
        minDeltaHeight = deltaHight
        minIndex = i
print(minIndex+1)