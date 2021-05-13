from collections import Counter
N = int(input())
S = list(input().split())
S = Counter(S)

if len(S) == 4:
    ans = "Four"
else:
    ans = "Three"

print(ans)
