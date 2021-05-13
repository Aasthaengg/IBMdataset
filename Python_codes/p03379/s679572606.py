n = int(input())
x = [int(i) for i in input().split()]
xs = sorted(x)
l = xs[n//2 -1]
r = xs[n//2]
for i in x:
    if i <= l:
        print(r)
    else:
        print(l)