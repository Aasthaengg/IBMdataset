N = int(input())
cur = 0
ans = 0
for c in input():
    if c == 'I':
        cur += 1
        ans = max(ans, cur)
    else:
        cur -= 1
print(ans)
