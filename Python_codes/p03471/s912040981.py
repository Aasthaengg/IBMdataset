N,X = map(int,input().split())
l = []
bo = 0
for a in range(N+1):
    for b in range(N-a+1):
        if a*10000 + b*5000 + (N-a-b)*1000 == X:
            T = [a,b,N-a-b]
            bo+=1
            break


if bo==0:
    print('-1 -1 -1')
else:print(*T,sep=' ')