import sys
N, *AB = [int(x) for x in input().split()]
As, Bs, Ag, Bg = map(lambda x : x - 1, AB)
S = input()
for (s, g) in [(As, Ag), (Bs, Bg)]:
    if '##' in S[s : g + 1]:
        print("No")
        sys.exit()

if Bg < Ag:  # AがBを飛び越える必要がある
    if '...' not in S[Bs - 1 : Bg + 2]:
        print("No")
        sys.exit()

print("Yes")