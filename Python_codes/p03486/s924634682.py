# B - Two Anagrams
s = list(input())
t = list(input())

# sを可能な限り辞書順で小さくする
s = sorted(s)
s = "".join(s)

# tを可能な限り辞書順で大きくする
t = sorted(t, reverse=True)
t = "".join(t)

# 一文字ずつ文字コードで比較する
ans = ""
N = min(len(s),len(t))
for i in range(N):
    if ord(s[i]) == ord(t[i]):
        pass
    elif ord(s[i]) < ord(t[i]):
        ans = "Yes"
        break
    else:
        ans = "No"
        break
else: #調べた文字が全部一緒だった場合、文字列の長さで比較
    if len(s) < len(t):
        ans = "Yes"
    else:
        ans = "No"

# 出力
print(ans)
