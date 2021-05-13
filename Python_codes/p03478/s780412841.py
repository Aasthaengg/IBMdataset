# input
N, A, B = map(int, input().split())

# check
res = sum([n for n in range(1, N + 1) if A <= sum(list(map(int, str(n)))) <= B])
print(res)