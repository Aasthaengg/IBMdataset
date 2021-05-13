n, m = map(int, input().split())
s = set(map(str, range(m+1)))
for _ in range(n):
    s &= set(input().split()[1:])
print(len(s))