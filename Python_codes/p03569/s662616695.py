s = list(map(str,input()))
l = len(s)
cntf = 0
cntl = l-1
ans = 0

while cntf < cntl:
    if s[cntf] == s[cntl]:
        cntf += 1
        cntl -= 1
    else:
        if s[cntf] == "x":
            ans += 1
            cntf += 1
        elif s[cntl] == "x":
            ans += 1
            cntl -= 1
        else:
            print(-1)
            exit()

print(ans)