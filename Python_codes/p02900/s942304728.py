A,B=map(int,input().split())
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
a=make_divisors(A)
b=make_divisors(B)
kouyakusuu=set(a)&set(b)
out=[]
kouho=sorted(list(kouyakusuu))
del kouho[0]
for a in range(len(kouho)-1):
    for b in range(a+1,len(kouho)):
        if kouho[b]%kouho[a]==0:
            out.append(kouho[b])
answer=set(out)
print(len(kouho)+1-len(answer))
