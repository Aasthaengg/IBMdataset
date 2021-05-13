n, x, y = map(int,input().split())
cnt = [0]*n

x -= 1
y -= 1

for i in range(n):
    for j in range(i+1, n):
        a = j - i
        b = abs(x - i) + 1 + abs(j - y)
        c = min(a, b)
        cnt[c] += 1
for i in range(1,n):
    print(cnt[i])
