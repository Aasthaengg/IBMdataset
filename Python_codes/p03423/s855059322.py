while True:
    N = int(input())
    if N >= 1 and N <= 1000:
        break
if N < 3:
    print(0)
if N >= 3:
    print(int(N/3))