S, T = input().split()
A, B = map(int, input().split())
d = dict(zip([S, T], [A, B]))
U = input()
d[U] -= 1
print(*d.values())
