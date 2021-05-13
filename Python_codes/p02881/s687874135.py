n=int(input())

def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

a=divisor(n)
a.sort()

c=[]
for i in range(len(a)//2+1):
    d=a[i]-1+a[-i-1]-1
    c.append(d)

print(min(c))