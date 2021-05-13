N, D = map(int, input().split())
breadth = 2 * D

ans = 0
while N > 0:
    N -= breadth + 1
    ans += 1
print(ans)
