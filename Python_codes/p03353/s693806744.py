s = input()
K = int(input())
N = len(s)
sets = set()
for l in range(1, K+1):
    for i in range(N-l+1):
        subs = s[i:i+l]
        sets.add(subs)

sets = sorted(list(sets))
print(sets[K-1])