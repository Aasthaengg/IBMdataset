# ε₯ε
A, B = map(int, input().split())

# εΊε
if A + B == 24:
    w = 0
elif A + B > 24:
    w = abs(24 - (A + B))
else:
    w = A + B


print(w)