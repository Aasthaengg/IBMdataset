s = list(input())

if len(s) == 2:
    print("".join(s))
else:
    ans = []
    for i in range(len(s)-1,-1,-1):
        ans.append(s[i])
    else:
        print("".join(ans))