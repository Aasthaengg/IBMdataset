N = int(input())
P = [int(x) for x in input().split()]

Min = float('inf')
cnt = 0
for i in range(N):
    if P[i] <= Min:
        cnt += 1
        Min = P[i]

print(cnt)