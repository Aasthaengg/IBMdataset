S = input().rstrip()

num_b = 0
ans = 0
for v in S:
    if v == 'B':
        num_b += 1
    else:
        ans += num_b

print(ans)