n = int(input())
S = [int(e) for e in input().split()]
q = int(input())
T = [int(e) for e in input().split()]

res = 0
for t in T:
    if t in S:
        res += 1

print(res)

