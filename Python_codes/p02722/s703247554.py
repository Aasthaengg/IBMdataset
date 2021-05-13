import math

def divisors(n):
    div = [n]
    for i in xrange(2,int(math.sqrt(n))+1):
        if n%i == 0:
            div.append(i)
            div.append(n/i)
    return div

n = int(raw_input())
ndiv = set(divisors(n))
mdiv = set(divisors(n-1))
count = 0
for x in ndiv:
    for k in xrange(1,41):
        if x**k > n:
            break
        if (n%x**k)==0 and (n/x**k)%x == 1:
            count += 1
            #print x
            break
count += len(mdiv)
if n==2:
    count = 1
print count