N = int(input())
a = N % 1000
if a == 0:
    print(0)
else:
    b = int(N / 1000)
    print((b + 1) * 1000 - N)
