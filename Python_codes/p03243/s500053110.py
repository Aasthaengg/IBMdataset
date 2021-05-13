# input
N = int(input())

for n in range(111, 1000, 111):
    if N <= n:
        print(n)
        exit(0)