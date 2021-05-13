# def rleify(s: str) -> List[Tuple[str, int]]:
def rleify(s):
    if not len(s):
        return []
    i = 0
    rle = []
    for j in range(len(s) + 1):
        if j == len(s) or s[i] != s[j]:
            rle.append((s[i], j - i))
            i = j
    return rle


s = input()
X, Y = map(int, input().split())
rle = rleify(s)
if rle[0][0] == "F":
    X -= rle[0][1]
    rle = rle[1:]
S = []
P = []
iss = True
for c, n in rle:
    if c == "T":
        if n % 2 == 1:
            iss = not iss
    else:
        if iss:
            S.append(n)
        else:
            P.append(n)

cand = {0}
for n in S:
    ncand = set()
    for c in cand:
        ncand.add(c - n)
        ncand.add(c + n)
    cand = ncand
if X not in cand:
    print("No")
    exit()

cand = {0}
for n in P:
    ncand = set()
    for c in cand:
        ncand.add(c - n)
        ncand.add(c + n)
    cand = ncand
if Y not in cand:
    print("No")
    exit()
print("Yes")
