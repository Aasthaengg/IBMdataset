N = int(input())
LP = list(map(int, input().split()))

cnt = 0
for i in range(N-2):
    LA = []
    LB = []
    LA.append(LP[i])
    LA.append(LP[i+1])
    LA.append(LP[i+2])
    LB = sorted(LA)
    if LA[1] == LB[1]:
        cnt += 1
print(cnt)