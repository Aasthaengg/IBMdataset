N, A, B = map(int, input().split())
res = 0
for num in range(N + 1):
    if A <= sum([int(x) for x in str(num)]) <= B:
        res += num
print(res)