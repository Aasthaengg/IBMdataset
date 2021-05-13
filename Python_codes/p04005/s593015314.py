from itertools import combinations

ABC = list(map(int, input().split()))
if any(x % 2 == 0 for x in ABC):
    print(0)
else:
    ans = float("inf")
    for a, b in combinations(ABC, 2):
        ans = min(ans, a * b)
    print(ans)
