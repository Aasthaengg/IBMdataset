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

a,b=map(int,input().split())
a=make_divisors(a)
b=make_divisors(b)
a=set(a)
b=set(b)
s=sorted(a&b)
ans=[1]
for i in s[1:]:
    switch=0
    for j in ans[1:]:
        if i%j==0:
            switch=1
            break
    if switch==0:
        ans.append(i)
print(len(ans))