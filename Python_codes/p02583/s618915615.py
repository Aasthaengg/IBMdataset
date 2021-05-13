import itertools
n = int(input())
l = list(map(int, input().split()))
ans = 0
for a,b,c in itertools.combinations(l,3):
    if abs(a-b) < c < a+b and len(set([a,b,c])) == 3:
        ans += 1
print(ans)