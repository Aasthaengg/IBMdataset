N=int(input())
x=1
while x*(x-1)//2<N:
    x+=1
if x*(x-1)//2>N:
    print('No')
else:
    print('Yes')
    print(x)
    a=[[] for i in range(x)]
    from itertools import combinations
    y=1
    for i,j in combinations(range(x),2):
        a[i].append(y)
        a[j].append(y)
        y+=1
    for l in a:
        print(x-1,*l)