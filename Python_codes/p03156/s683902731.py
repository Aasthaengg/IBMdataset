n = int(input())
a, b = map(int, input().split())
P = list(map(int, input().split()))

problem = [0, 0, 0]
for p in P:
    if p <= a:
        problem[0] += 1
    elif p <= b:
        problem[1] += 1
    else:
        problem[2] += 1

print(min(problem))