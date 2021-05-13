n, a, b = map(int, input().split())
S = []
for i in range(1, n+1):
    if a <= sum([int(x) for x in list(str(i))]) <= b:
        S.append(i)
print(sum(S))