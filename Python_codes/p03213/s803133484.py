def sieve(n):
    prime=[]
    limit=n**0.5
    data=[i+1 for i in range(1,n)]
    while True:
        p=data[0]
        if limit<=p:
            return prime+data
        prime.append(p)
        data=[e for e in data if e%p!=0]

def main():
    n=int(input())
    primes=sieve(n+1)
    l=len(primes)

    factor=[]
    for i in range(l):
        p = primes[i]
        cnt = 0
        fac = p
        while fac <= n:
            cnt += n//fac
            fac *= p
        factor.append(cnt)
    
    l2=len(factor)
    idx=[0,0,0,0,0]
    fac=[2,4,14,24,74]
    j,i=4,0
    while i<l2:
        if  factor[i] < fac[j]:
            idx[j] = i
            j-=1
            if j==-1:
                break
        else:
            i+=1

    ans=idx[4]+idx[3]*max(0,idx[0]-1)+idx[2]*max(0,idx[1]-1)+idx[1]*max(0,idx[1]-1)*max(0,idx[0]-2)//2
    print(ans)

if __name__=='__main__':
    main()