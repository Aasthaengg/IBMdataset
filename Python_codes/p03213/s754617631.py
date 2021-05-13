n=int(input())

N=[0]*(n+1)

def f(n):
    M=[]
    while n%2==0:
        n//=2
        M.append(2)
    i=3
    while n>=i:
        while n%i==0:
            n//=i
            M.append(i)
        i+=2
    return M

for i in range(2,n+1):
    for j in f(i):
        N[j]+=1

def num(m):
    return len(list(filter(lambda x:x>=m-1,N)))

print(num(75)+num(25)*(num(3)-1)+num(15)*(num(5)-1)+num(5)*(num(5)-1)*(num(3)-2)//2)