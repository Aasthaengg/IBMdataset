S = input().rstrip()

cur_b = 0

ans = 0
for s in S:
    if s == 'B':
        cur_b += 1
    else:
        ans += cur_b

print(ans)