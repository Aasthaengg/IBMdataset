N = int(input())
D, X = map(int, input().split())
A = [int(input()) for i in range(N)]

ans = X + N
for i in A:
    day = 1
    while True:
        day += i
        if day <= D:
            ans += 1
        else:
            break
print(ans)
