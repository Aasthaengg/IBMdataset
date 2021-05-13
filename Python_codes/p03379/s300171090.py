n = int(input())
x = [int(i) for i in input().split()]
sx = sorted(x)
s1, s2 = sx[n//2-1], sx[n//2]
m = (s1 + s2) / 2
for i in x:
    if m > i: print(s2)
    else: print(s1)
