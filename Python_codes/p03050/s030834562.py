import math

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

#a = list(map(int, input().split()))

#####################################


#2:10
n=int(input())
a=make_divisors(n)
ans=0
for i in range(len(a)):
    if(a[i]<n//a[i]-1):
        ans+=n//a[i]-1
print(ans)