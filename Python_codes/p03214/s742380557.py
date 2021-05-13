n = int(input())
al = list(map(int,input().split()))

mean = sum(al) / n

argmin = -1
min_a = float("inf")

for idx, a in enumerate(al):
    if min_a > abs(mean-a):
        argmin = idx
        min_a = abs(mean-a)

print(argmin)