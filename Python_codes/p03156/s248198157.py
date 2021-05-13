N = int(input())
A, B = map(int, input().split())
P = map(int, input().split())

memo = [0]*3
for e in P:
    if e <= A:
        memo[0] += 1
    elif e <= B:
        memo[1] += 1
    else:
        memo[2] += 1
print(min(memo))

