n = int(input())
s = input()

m = 0

for i in range(1, n):
    t = set(s[:i])
    u = set(s[i:])
    m = max(len(t & u), m)

print(m)