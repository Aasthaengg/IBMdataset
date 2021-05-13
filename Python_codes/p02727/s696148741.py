x, y, A, B, C = map(int, input().split())
r  = list(map(int, input().split()))
b  = list(map(int, input().split()))
mu = list(map(int, input().split()))

mu += sorted(r)[-x:]
mu += sorted(b)[-y:]
print(sum(sorted(mu)[-(x+y):]))
