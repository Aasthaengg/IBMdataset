import decimal,math
decimal.getcontext().prec = 100
def sum1(pre,l,r):
    l=max(l,0)
    if(l==0):
        return pre[r]
    return pre[r] - pre[l - 1]
abc=[]
def printDivisors(n) : 
    i = 1
    while i <= math.sqrt(n): 
          
        if (n % i == 0) : 
              
            if (n / i == i) : 
                abc.append(i) 
            else : 
                abc.append(i)
                abc.append(n/i)
        i = i + 1
n,k=map(int,raw_input().split())

arr=map(int,raw_input().split())
s=sum(arr)
printDivisors(s)
abc.sort()
abc=abc[::-1]
ans=1
for i in abc:
    l=0
    flag=0
    c=[]
    for j in arr:
        c.append(j%i)
    c.sort()
    if(sum(c[:-sum(c)/i])<=k):
        print i
        exit()