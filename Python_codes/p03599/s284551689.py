import itertools

a,b,c,d,e,f = map(int,input().split())

A = list(range(0,101))
B = list(range(0,101))
ptr = list(itertools.product(A, repeat=2))
ptr2 = list(itertools.product(B, repeat=2))

tmp = 0
ans = [0,0]

for a1,b1 in ptr:
    for c1,d1 in ptr2:
        if (a*a1+b*b1) * e >= c * c1 + d * d1 and (a*a1+b*b1) * 100 + c * c1 + d * d1 <= f:
            if tmp*(a*a1+b*b1) <= (c * c1 + d * d1) and not (a1 == 0 and b1 == 0 and c1 == 0 and d1 == 0):
                tmp = (c * c1 + d * d1)/(a*a1+b*b1)
                ans = [(a*a1+b*b1) * 100 + c * c1 + d * d1, c * c1 + d * d1]

print(ans[0], ans[1])
