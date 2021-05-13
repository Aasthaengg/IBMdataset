n, m, x = map(int, input().split())
a = [i for i in map(int, input().split()) if i < x]
print(min(len(a), m - len(a)))