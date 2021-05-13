N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]

max = 0
for c in S:
    money = S.count(c) - T.count(c)
    if money > max:
        max = money
print(max)