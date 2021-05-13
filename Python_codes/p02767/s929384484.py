n = int(input())
x = list(map(int, input().split()))

ans = float('inf')
for i in range(1, 101):
    h = 0
    for j in x:
        h += (i-j)**2
    ans = min(ans, h)
print(ans)