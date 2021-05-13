from scipy.special import comb

N, P = map(int, input().split())
A = list(map(int, input().split()))

o,e = 0,0
for a in A:
    if a%2==0:
        e+=1
    else:
        o+=1

if P == 0:
    # select even cnt from o
    t = 0
    for i in range(0, o+1, 2):
        t += comb(o, i, True)
    print(2**e * t)
else:
    t = 0
    for i in range(1, o+1, 2):
        t += comb(o, i, True)
    print(2**e * t)



