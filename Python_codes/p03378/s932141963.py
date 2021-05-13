_, m, x = map(int, input().split())
(*a,) = map(int, input().split())
r = sum(x < i for i in a)
print(min(r, m - r))