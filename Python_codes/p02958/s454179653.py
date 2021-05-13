N=int(input())
p=list(map(int,input().split()))

k=0
for x,y in zip(p,sorted(p)):
    if x!=y:
        if k>2:
            break
        k+=1

if k>2:
    print('NO')
else:
    print('YES')
