N = int(input())
P = list(map(int, input().split()))
ans = 0
for i in range(N-2):
    ans += P[i] < P[i+1] < P[i+2]
    ans += P[i] > P[i+1] > P[i+2]
print(ans)
