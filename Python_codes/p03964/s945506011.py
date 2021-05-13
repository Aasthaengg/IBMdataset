n = int(input())

tlist = [list(map(int,input().split())) for i in range(n)]

a = tlist[0][0]
b = tlist[0][1]

for t in tlist:
    multi = max((a//t[0]) + (a%t[0] > 0), (b//t[1]) + (b%t[1] > 0))
    # print('multi', multi)
    # print('a b', a, b)
    a = t[0]*multi
    b = t[1]*multi

print(a + b)
