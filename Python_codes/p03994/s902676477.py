def c2a(c):
    return (26 - ord(c) + ord("a")) % 26


s = input()
k = int(input())
l = len(s)
ans = ""
for i, e in enumerate(s, 1):
    if i == l:
        code = (ord(e) - ord("a") + k) % 26 + ord("a")
        c = chr(code)
    else:
        cnt = c2a(e)
        if cnt <= k:
            c = "a"
            k -= cnt
        else:
            c = e

    ans += c

print(ans)
