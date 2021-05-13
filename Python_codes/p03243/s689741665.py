N = int(input())
for n in range(N, 1000):
    if len(set(str(n))) == 1:
        print(n)
        break