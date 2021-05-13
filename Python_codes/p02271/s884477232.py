from functools import lru_cache

n = int(input())
A = sorted(list(map(int, input().split())))
q = int(input())
query = list(map(int, input().split()))

@lru_cache(maxsize=None)
def solve(i, m):
    if m == 0:
        return True
    elif i >= n or m < A[i]:
        return False
    else:
        return solve(i + 1, m - A[i]) or solve(i + 1, m)

for m in query:
    if solve(0, m):
        print("yes")
    else:
        print("no")