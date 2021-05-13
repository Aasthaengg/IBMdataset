s = list(input())
ls = len(s)
ss = sorted(s, reverse=True)
cnt = [0, 0]
ans = 0
w = 0

while ss[w] == "W":
    w += 1
    if ls == w:
        break

for i in range(ls):
    if s[i] == "B":
        ans += w + cnt[0] - i
    else:
        ans += i - cnt[1]
    cnt[s[i] != "B"] += 1

print(ans//2)
