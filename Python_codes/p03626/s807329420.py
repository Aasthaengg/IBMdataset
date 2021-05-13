mod = 1000000007
with open(0) as f:
    N, s, t = f.read().split()

#ドミノの並べ方を0,1で整理
domino = []
s += '_'
c = s[0]
lying = False
for x in s[1:]:
    if x == c:
        lying = True
        continue

    if lying:
        domino.append(1)
    else:
        domino.append(0)
    c = x
    lying = False

#初期値
if domino[0] == 0:
    ans = 3
else:
    ans = 6
#右へ走査
for idx,d in enumerate(domino[1:]):
    if domino[idx] == 0:
        ans *= 2
    else:
        if d == 0:
            ans *= 1
        else:
            ans *= 3
    ans %= mod
print(ans)