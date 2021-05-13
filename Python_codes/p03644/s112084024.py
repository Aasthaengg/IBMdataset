N = int(input())
for i in range(6, -1, -1):
    if 2**i > N:
        continue
    print(2**i)
    break