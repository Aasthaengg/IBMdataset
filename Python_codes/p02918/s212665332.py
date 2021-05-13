#ika tako

n, k = list(map(int, input().split()))
s = input()
group = 1
for c, d in zip(s, s[1:]):
    if c != d:
        group += 1
print(n - max(1, group - 2 * k))