s = input()
ans = 1
num = 1 #文字数

if len(s) == 1:
    print(1)
    exit()


for i in range(1, len(s)):
    if num == 1:
        if s[i - 1] != s[i]:
            ans += 1
        else:
            if i != len(s) - 1:
                num = 2
                ans += 1
    elif num == 2:
        num = 1.5
    elif num == 1.5:
        ans += 1
        num = 1
print(ans)