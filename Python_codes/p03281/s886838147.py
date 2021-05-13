def divisors(n):
    lower_divisors=[]
    upper_divisors=[]
    i=1
    while i*i<=n:
        if n%i==0:
            lower_divisors.append(i)
            if i!=n//i:
                upper_divisors.append(n//i)
        i+=1
    return lower_divisors+upper_divisors[::-1]

n=int(input())
cnt=0
for i in range(1,n+1,2):
    if len(divisors(i))==8:
        cnt+=1
print(cnt)