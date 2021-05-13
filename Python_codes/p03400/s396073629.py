N = int(input())
D, X = map(int, input().split())
ans = 0
for i in range(N):
    A = int(input())
    j = 0
    while True:
        if 1 + A * j <= D: 
            ans += 1
            j += 1
        else:
            break

print(ans + X)
