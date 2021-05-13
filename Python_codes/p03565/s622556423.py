s = list(input())
t = list(input())
ls = len(s)
lt = len(t)
ans = ["UNRESTORABLE"]

if "?" not in set(s):
    print("".join(s))
    exit()

for i in range(ls-lt+1):
    f = True
    for j in range(lt):
        f &= (s[i + j] == "?" or s[i + j] == t[j])

    if f:
        ans = s.copy()
        for j in range(lt):
            ans[i+j] = t[j]


print("".join(ans).replace("?", "a"))
