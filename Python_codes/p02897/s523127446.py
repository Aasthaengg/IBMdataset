# input
N = int(input())

if N % 2 == 0:
    print(0.5)
elif N == 1:
    print(1)
else:
    c = (N - 1) // 2
    print((c + 1) / N)