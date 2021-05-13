S = input()
K = int(input())
N = len(S)
substrs = set()

for i in range(N):
    cur = S[i]
    if cur not in substrs:
        substrs.add(cur)
    for j in range(i + 1, min(N, i + 6)):
        cur += S[j]
        if cur not in substrs:
            substrs.add(cur)

substrs = sorted(substrs)
print(substrs[K - 1])
