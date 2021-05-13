

n = int(input())
leafNums = list(map(int, input().split()))

ans = 0

# d=0
ans += 1
currentRootNodeNum = 1
if (leafNums[0] >= 1 and n >=1) or (leafNums[0] > 1 and n == 0):
    print(-1)
    exit()

# cond2maxの計算でTLEっぽいので、事前に累積和を求めておく
leafAccumlateFromEnd = [0] * (n+1)
leafAccumlateFromEnd[n] = leafNums[n]
for i in range(n-1,-1,-1):
    leafAccumlateFromEnd[i] = leafAccumlateFromEnd[i+1] + leafNums[i]

# d=1~n
for i in range(1, n+1):
    # cond2max = sum(leafNums[i:])
    cond2max = leafAccumlateFromEnd[i]
    cond1max = currentRootNodeNum*2
    currentMax = min(cond1max, cond2max)
    ans += currentMax
    currentRootNodeNum = currentMax - leafNums[i]
    if currentRootNodeNum < 0:
        print(-1)
        exit()

print(ans)