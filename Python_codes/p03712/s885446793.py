H, W = map(int, input().split())
S = []
x = '#' * (W + 2)
for _ in range(H):
    s = input()
    S.append('#' + s + '#')

print(x)
for s in S:
    print(s)
print(x)

