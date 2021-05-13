def make_divisors(n):
    a,b =[],[]
    i = 1
    while i*i<=n:
        if n%i == 0:
            a.append(i)
            if i != n//i:
                b.append(n//i)
        i+= 1
    return a+b[::-1]

n = int(input())
c = 0
for i in range(1,n+1):
    if len(make_divisors(i))== 8 and i%2==1:
        c+=1
print(c)