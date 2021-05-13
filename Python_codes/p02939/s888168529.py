s = input()
ans = 0
i = 0
before = '#'
while(i<len(s)):
    if(s[i]!=before):
        before = s[i]
        i += 1
        ans += 1
    else:
        before = '#'
        i += 2
        ans += 1

if(i!=len(s)):
    ans -= 1

print(ans)