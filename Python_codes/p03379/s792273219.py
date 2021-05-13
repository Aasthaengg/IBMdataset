import statistics

N = int(input())
xl = list(map(int, input().split()))

small = statistics.median_low(xl)
big = statistics.median_high(xl)
#print(small,big)
for i in range(N):
    if xl[i] <= small:
        print(big)
    else:
        print(small)
