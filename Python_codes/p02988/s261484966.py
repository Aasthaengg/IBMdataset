N = int(input())
P = list(map(int, input().split()))
cnt = 0
for n in range(N-2):
    if P[n] < P[n+1] < P[n+2] or P[n+2] < P[n+1] < P[n]:
        cnt += 1
print(cnt)
