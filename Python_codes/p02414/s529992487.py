n,m,l = list(map(int,input().split()))
A = [list(map(int,input().split())) for i in range(n)]
B = [map(int,input().split()) for i in range(m)]
B_T = list(map(list, zip(*B)))
for a in A:
    row = []
    for b in B_T:
        row.append(sum([x*y for (x,y) in zip(a,b)]))
    print(' '.join(map(str,row)))