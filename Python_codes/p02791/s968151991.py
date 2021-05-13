N = int(input())
P = list(map(int, input().split()))

res = 0
mini = P[0]
for i in range(N):
    mini = min(mini, P[i])
    if(mini >= P[i]):
        res += 1
print(res)
