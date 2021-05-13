N=int(input())

def make_divisors(n):
    divisors = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)

    return divisors

l=make_divisors(N)
ans=0
for i in range(len(l)):
    num=l[i]-1
    if num==0:
        continue
    if num==1:
        continue
    p=N//num
    q=N%num
    if p==q:
        ans+=num 
print(ans)