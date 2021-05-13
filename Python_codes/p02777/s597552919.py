s, t = map(str, input().split())
a, b = map(int, input().split())
u = input()
d = {}
d[s] = a
d[t] = b
d[u] -= 1
print(d[s], d[t])