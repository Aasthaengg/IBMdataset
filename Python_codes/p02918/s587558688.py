n, k = map(int, input().split())
s = input()
sep = sum(a != b for a, b in zip(s, s[1:]))
print(n - max(0, sep - 2 * k) - 1)