N = int(input())
x = list(map(int, input().split()))
sx = sorted(x)
a = sx[N//2-1]
b = sx[N//2]

for c in x:
    if c <= a:
        print(b)
    else:
        print(a)