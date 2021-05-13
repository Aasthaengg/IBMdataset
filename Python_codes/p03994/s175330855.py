S = input()
K = int(input())

ans = ""
for s in S:
    if s == "a":
        ans += s
    elif 123-ord(s) <= K:
        ans += "a"
        K -= 123-ord(s)
    else:
        ans += s
if K > 0:
    ans = ans[:-1] + chr((ord(ans[-1])-97+K)%26+97)
print(ans)
