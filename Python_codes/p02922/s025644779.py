a, b = map(int, input().split())

ans = 0
start = 1
for i in range(21):
    if start >= b:
        ans = i
        break
    start -= 1
    start += a

print(ans)
