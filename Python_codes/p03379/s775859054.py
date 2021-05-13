n = int(input())
x = list(map(int, input().split()))
sx = sorted(x)
m = n//2
l = sx[m - 1: m + 1]

for i in range(n):
    if x[i] < l[1]:
        print(l[1])
    else:
        print(l[0])