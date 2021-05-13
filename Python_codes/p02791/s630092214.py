N = int(input())
P = list(map(int, input().split()))
min_p = 1000000
answer= 0
for i in range(N):
    if P[i] <= min_p :
        answer += 1
        min_p = P[i]
print(answer)