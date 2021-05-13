import itertools
S = input()
ans = 0
for i,j in itertools.combinations(range(len(S)+1), 2):
    if all('ACTG'.count(c)==1 for c in S[i:j]):
        ans = max(ans, len(S[i:j]))
print(ans)
