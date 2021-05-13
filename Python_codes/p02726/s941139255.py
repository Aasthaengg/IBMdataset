n, x, y = map(int, input().split())
ans = [0] * (n - 1)

x -= 1
y -= 1
for i in range(n):
    for j in range(n):
        c = min(abs(i - j), abs(i-x)+abs(j-y)+1,abs(i-y)+abs(j-x)+1)
        if c:
            ans[c-1] += 1

for ai in ans:
    print(ai//2)
