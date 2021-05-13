n = int(input())
l = [list(map(int,input().split())) for i in range(n)]
a,b = [list(i) for i in zip(*l)]
x = 0
for i in range(n)[::-1]:
    if (a[i] + x) % b[i] != 0:
        x += b[i] - ((a[i] + x)  % b[i])
print(x)