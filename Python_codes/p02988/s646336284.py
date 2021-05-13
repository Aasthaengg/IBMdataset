n = int(input())
P = [int(i) for i in input().split()]

ans = 0
for i in range(1, n-1):
    if P[i-1] < P[i] < P[i+1]:
        ans += 1
    elif P[i-1] > P[i] > P[i+1]:
        ans += 1
print(ans)