s = list(input())
ans = 0
while len(s) > 1:
    if s[0] == s[-1]:
        del s[0]
        del s[-1]
    else:
        if s[0] == "x":
            del s[0]
            ans += 1
        elif s[-1] == "x":
            del s[-1]
            ans += 1
        else:
            print(-1)
            exit()
print(ans)