def divisors(n):
    d=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            d.append(i)
            if i!=n//i:
                d.append(n//i)
    d.sort()
    return d
a=0
for i in range(1,int(input())+1):
    a+= i%2 and len(divisors(i))==8
print(a)