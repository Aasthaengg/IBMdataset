n, k, w = int(input()), int(input()), 1
for _ in range(n):
    w += min(w, k)
print(w)