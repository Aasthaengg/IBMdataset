s = input()
"""
xabxa
"""
l = 0
r = len(s)-1
cnt = 0
while r - l >= 1:
    if s[r] == s[l]:
        l += 1
        r -= 1
    else:
        if s[l] == "x":
            l += 1
            cnt += 1
        elif s[r] == "x":
            r -= 1
            cnt += 1
        else:
            print(-1)
            exit()
print(cnt)        
