s = input()
ans = 0
B = 0
for x in s:
    if x == 'B':
        B += 1
    else:
        ans += B
print(ans)
