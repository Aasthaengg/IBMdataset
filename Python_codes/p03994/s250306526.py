S = input()
K = int(input())

oz = ord("z")

ans = ""

for s in S[:-1]:
    if s != "a" and oz+1-ord(s) <= K:
        K -= oz+1-ord(s)
        ans += "a"
    else:
        ans += s

ans += chr(((ord(S[-1])-ord("a")+K)%26)+ord("a"))

print(ans)