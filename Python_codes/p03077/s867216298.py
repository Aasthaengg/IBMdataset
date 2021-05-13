l = [int(input()) for _ in range(6)]

m = min(l[1:])

mc = l[0] // m
mr = l[0] % m

if mr != 0:
    mc += 1

print( 4 + mc )