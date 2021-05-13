n,a,b = [int(i) for i in input().split(' ')]
ab = a+b
c = n < ab
r = ab - n if c else 0
print(' '.join([str(i) for i in [min(a,b), r]]))
