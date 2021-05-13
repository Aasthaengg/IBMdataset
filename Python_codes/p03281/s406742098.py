n=int(input())

def count_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return len(lower_divisors + upper_divisors[::-1])


ans=0
for i in range(1,n+1):
    if i%2==1:
        c=count_divisors(i)
        if c==8:
            ans+=1
            #print(i)
print(ans)