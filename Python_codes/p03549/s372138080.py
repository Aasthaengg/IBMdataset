n, m = map(int, input().split())
t = 1900*m + 100*(n-m)
p = (2)**m
print(t*p)