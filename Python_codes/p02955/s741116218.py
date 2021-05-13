#ある数gを用意して，最も近いgの倍数にするための手数を数える，プラマイの総和が0にならない限り，最も変更に要する手数が大きいところは逆転させる？
#gはAの総和の約数

N,K=map(int,input().split())
A=list(map(int,input().split()))


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

div=make_divisors(sum(A))

ans=0
for g in div:
    near=[0]*N
    S=0
    for i in range(N):
        near[i]=a=A[i]%g
        S+=near[i]
    near.sort()
    ii=0
    while S!=0:
        S-=g
        ii-=1
    temp=sum(near[:ii])
    if temp<=K:
        ans=max(ans,g)
        
print(ans)
    
    


