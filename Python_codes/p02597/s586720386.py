n = int(input())
s = input()
l = 0
r = n-1
ans = 0
while l < r:
    # print(l, r)
    if s[l] == 'W':
        if s[r] == 'W':
            r -= 1
        elif s[r] == 'R':
            r -= 1
            l += 1
            ans += 1
    elif s[l] == 'R':
        if s[r] == 'W':
            r -= 1
            l += 1
        elif s[r] == 'R':
            l += 1
print(ans)
