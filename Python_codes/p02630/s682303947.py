_ = input()
a = list(map(int, input().split()))

counts = [0] * (10 ** 5 + 1)
for ai in a:
    counts[ai] += 1

s = sum(a)
q = int(input())
for i in range(q):
    b, c = map(int, input().split())
    s += (c - b) * counts[b]
    print(s)
    counts[c] += counts[b]
    counts[b] = 0