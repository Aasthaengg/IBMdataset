n = int(input())
s = list(input())
b = [0] * n
w = [0] * n
x,y = 0,0
ans = 0
for i in range(n):
    if s[i] == '#':
        x += 1
    else:
        y += 1
    b[i] = x
    w[i] = y

ans = float('inf')
for i in range(n):
    ans = min(ans, b[i] + w[n-1] - w[i])
print(min(ans, b[n-1], w[n-1]))