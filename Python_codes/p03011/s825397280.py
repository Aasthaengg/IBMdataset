P = list(map(int, input().split()))
a = P.pop(P.index(min(P)))
b = P.pop(P.index(min(P)))
print(a + b)
