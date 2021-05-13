s = input()
l,r = 0, len(s)-1
res = 0
if s==s[::-1]:
    print(res)
    exit()

while l<r:
    if s[l]==s[r]:
        l += 1
        r -= 1
    else:
        if l==r:
            print(res)
            break
        elif s[l]!='x' and s[r]!='x':
            print(-1)
            break
        elif s[l]=='x':
            l += 1
            res += 1
        elif s[r]=='x':
            r -= 1
            res += 1
else:
    print(res)