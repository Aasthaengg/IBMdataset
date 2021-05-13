N = input()
R = [input() for i in range(N)]

min_v = float("inf")
ans = -float("inf")
for r in R:
    ans = max(ans, r - min_v)
    min_v = min(min_v, r)
    
print ans