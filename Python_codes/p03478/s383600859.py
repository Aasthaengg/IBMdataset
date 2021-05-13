N, A, B = map(int, input().split())
r = 0
for n in range(1, N+1):
    if A <= sum([int(i) for i in str(n)]) <= B:
        r += n
print(r)
