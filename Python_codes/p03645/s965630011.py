n,m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
start = []
goal = []
for a,b in ab:
    if a == 1: start.append(b)
    elif b == n: goal.append(a)
print("POSSIBLE" if list(set(start) & set(goal)) else "IMPOSSIBLE")