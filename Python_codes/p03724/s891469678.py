from itertools import accumulate

N, M, *ab = map(int, open(0).read().split())
acc = [0] * (N + 1)
for a, b in zip(*[iter(ab)] * 2):
    if a > b:
        a, b = b, a
    acc[a - 1] += 1
    acc[b - 1] -= 1
acc = list(accumulate(acc, initial=0))
print("NO") if any(a % 2 for a in acc) else print("YES")
