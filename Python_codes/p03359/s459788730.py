a, b = map(int, input().split())

cnt = a - 1
ans = cnt + 1 if a <= b else cnt
print(ans)
