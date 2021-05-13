n = int(input())
s = input()
l = 0
r = s.count('.')
# if s[0] == '#':
#     l += 1
# else:
#     r -= 1
ans = float('inf')
for i in range(n-1):
    if s[i] == '#':
        l += 1
    else:
        r -= 1
    ans = min(ans, l+r)
    # print(ans, l, r)
ans = min(ans, s.count('.'))
ans = min(ans, s.count('#'))
print(ans)
