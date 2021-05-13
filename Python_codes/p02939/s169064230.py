s = input()
ans = 1
cur = s[0]
temp = 1
if len(s) != 2:
    while temp != len(s):
        if s[temp] != cur:
            if temp != len(s)-2:
                ans += 1
                cur = s[temp]
                temp += 1
            else:
                if s[temp] == s[temp+1]:
                    ans += 1
                    temp += 2
                else:
                    ans += 1
                    cur = s[temp]
                    temp += 1
        else:
            ans += 1
            cur = s[temp]+s[temp+1]
            temp += 2
    print(ans)
else:
    if s[0] == s[1]:
        print(1)
    else:
        print(2)
