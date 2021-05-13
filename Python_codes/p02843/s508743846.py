from itertools import combinations_with_replacement as C

X = int(input())
mono = [100, 101, 102, 103, 104, 105]
ans = 0
if X >= 2000:
    ans = 1
else:
    for i in range(1, 19 + 1):
        L = list(C(mono, i))
        for L in L:
            if sum(L) == X:
                ans = 1
                break

print(ans)