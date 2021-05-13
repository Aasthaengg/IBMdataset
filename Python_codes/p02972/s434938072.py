def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


n=int(input())
a=list(map(int,input().split()))

cnt=[0]*n
lst=[]

for i in range(n,0,-1):
    if cnt[i-1]%2==a[i-1]:
        continue
    
    else:
        lst.append(str(i))
        xxx=make_divisors(i)

        for j in xxx:
            cnt[j-1]+=1


print(len(lst))

if len(lst)>0:
    print(' '.join(lst))