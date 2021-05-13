alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
ss = input()
ans = ""
for s in ss:
    pos = alpha.index(s)
    pos = (pos + n) % 26
    ans += alpha[pos]
print(ans)