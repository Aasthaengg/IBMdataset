S = input()
L = list(S)
N = len(L)
bitmask = 2 ** (N - 1)

totals = []
for mask in range(bitmask):
    total = 0
    digit = 0
    for i in range(N):
        num = int(L[N - i - 1])
        total += num * (10 ** digit)
        # bitにi番目のフラグが立っているかどうか
        if mask & (1 << i):
            digit = 0
        else:
            digit += 1
    totals.append(total)

print(sum(totals))