from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


n,m=map(int,input().strip().split(" "))
fact=sorted(factors(m),reverse=True)
ans=1
for i in fact:
    if m//i >=n:
        ans=i
        break
print(ans)
