from itertools import combinations

N = int(input())
L = list(map(int, input().split()))
ans = 0
for v in combinations(L, 3):
    if len(set(v)) == 3:
        a, b, c = v
        if a + b > c and c + a > b and b + c > a:
            ans += 1
print(ans)