import string
S = input()
K = int(input())
LEN = len(S)
ans = ''
for pos, s in enumerate(S, 1):
    idx = string.ascii_lowercase.find(s)
    if pos < LEN:
        if idx > 0 and 26-idx <= K:
            ans += 'a'
            K -= (26 - idx)
        else:
            ans += s
    else:
        # 残りのKをすべて消費する
        ans += string.ascii_lowercase[(idx + K)%26]

print(ans)