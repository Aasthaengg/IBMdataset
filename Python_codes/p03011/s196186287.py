P, Q, R = map(int, input().split())
ans = P + Q + R - max([P, Q, R])
print(ans)