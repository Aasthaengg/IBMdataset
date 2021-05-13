N,K=(int(x) for x in input().split(" "))
def comb(n):
    return int(n*(n-1)/2)
limit=comb(N-1)
max=comb(N)

if K>limit:
    print (-1)
else:
    print (max-K)
    a=0
    for i in range (1,N+1):
        for j in range (i+1,N+1):
            if a<max-K:
                a+=1
            else:
                break
            c=str(i)
            d=str(j)
            print (c+" "+d)
        if a>=max-K:
            break