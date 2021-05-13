N = int(input())

maxL = [0] * (N+1)
maxR = [0]*(N+1)
num = []
for i in range(N):
    num.append(int(input()))
    maxL[i+1] = maxL[i] if maxL[i] > num[i] else num[i]

for i in range(N-1, 0, -1):
    maxR[i-1] = maxR[i] if maxR[i] > num[i] else num[i]

for i in range(N):
    print(max(maxL[i], maxR[i]))
