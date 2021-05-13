n = int(input())
a = [int(input()) for _ in range(n)]
sort_a = sorted(a, reverse=True)
amax = sort_a[0]
asecond = sort_a[1]
for i in range(n):
    tmp = a[i]
    if tmp == amax:
        print(asecond)
    else:
        print(amax)