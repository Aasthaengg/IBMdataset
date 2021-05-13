r, g, b, n = map(int, input().split())
ans = 0
for i in range(0, n+1, r):
    for j in range(0, n+1, g):
        if n < (i+j):
            break
        elif (n-(i+j))%b == 0:
            ans += 1

print(ans)