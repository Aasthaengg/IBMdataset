s = input()
n = len(s)
B_count = 0
ans = 0
for i in range(n):
    if s[i] == 'B':
        B_count += 1
    else:
        ans += B_count
print(ans)
