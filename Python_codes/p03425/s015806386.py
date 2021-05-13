from collections import Counter
N = int(input())

march = ("M", "A", "R", "C", "H")
cnt = Counter()
for _ in range(N):
    S = input()
    if S[0] in march:
        cnt[S[0]] += 1

res = 0

for m in range(2):
    for a in range(2):
        for r in range(2):
            for c in range(2):
                for h in range(2):
                    if m+a+r+c+h == 3:
                        x = 1
                        if m:
                            x *= cnt["M"]
                        if a:
                            x *= cnt["A"]
                        if r:
                            x *= cnt["R"]
                        if c:
                            x *= cnt["C"]
                        if h:
                            x *= cnt["H"]
                        res += x

print(res)