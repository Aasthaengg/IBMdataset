K = int(input())

print("50")
ans = []
a, b = divmod(K, 50)
for i in range(b):
    ans.append(49 + a + 50 - (b - 1))
for i in range(50-b):
    ans.append(49 + a - b)
print(" ".join([str(_) for _ in ans]))