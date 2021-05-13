H = int(input())
W = int(input())
N = int(input())

ans = 0
m = max([H, W])
while N > 0:
    N -= m
    ans += 1

print(ans)

