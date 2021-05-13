MOD = 10 ** 9 + 7
N = int(input())
S = iter(input() + " ")
prev = next(S)
count = 0
counts = []
for c in S:
    count += 1
    if prev != c:
        counts.append(count)
        count = 0
    prev = c
counts = iter(counts)
prev = next(counts)
ans = 3 * prev
for count in counts:
    if prev == 1:
        ans *= 2
    elif count == 2:
        ans *= 3
    prev = count
print(ans % MOD)