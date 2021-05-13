N = int(input())
d, X = map(int, input().split())
a = [int(input()) for _ in range(N)]
ans = 0
for i in range(N):
    cnt = 1
    for j in range(1,101):
        if a[i]*j + 1 <= d:
            cnt += 1
        else:
            ans += cnt 
            break

print(X+ans)