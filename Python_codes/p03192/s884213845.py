N = str(input())

num = 0
ln = len(N)
for nn in range(ln):
    if N[nn] == "2":
        num = num + 1
print(num)
