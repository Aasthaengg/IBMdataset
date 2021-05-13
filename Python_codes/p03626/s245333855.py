n = int(input())
s1 = list(input())
s2 = list(input())
if s1[0] == s2[0]:
    ans = 3
    i = 1
    flg = "x"
else:
    ans = 6
    i = 2
    flg = "y"
while i < n:
    if s1[i] == s2[i]:
        if flg == "x":
            ans *= 2
        else:
            flg = "x"
        i += 1
    else:
        if flg == "x":
            ans *= 2
            flg = "y"
        else:
            ans *= 3
        i += 2
    ans %= 10 ** 9 + 7
print(ans)