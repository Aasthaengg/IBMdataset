from itertools import accumulate
max2 = lambda x,y: x if x > y else y
min2 = lambda x,y: x if x < y else y

N = int(input())
S = input()

res = 0
for i in range(1,N):
    m = 0
    r = 0
    for a,b in zip(S,S[i:]):
        if a == b:
            r += 1
        else:
            r = 0
        m = max2(m,r)
    m = min2(m,i)
    res = max2(res, m)

print(res)

