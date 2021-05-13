N, K = map(int, input().split())
logs = list(map(int, input().split()))
maxL = max(logs)

minz = 0
maxz = maxL+1
while minz < maxz-1:
    midz = (maxz + minz)//2
    ncut = 0
    for i in range(N):
        thiscut = int((logs[i] + midz - 1) / midz) - 1
        ncut += thiscut

    if ncut > K:
        minz = midz
    else:
        maxz = midz

print(maxz)