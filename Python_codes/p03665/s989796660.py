n,p=map(int,input().split())
a=list(map(int, input().split()))

a_new=[]
for i in range(n):
    a_new.append(a[i]%2)
even=a_new.count(0)
odd=a_new.count(1)

if odd==0 and p==0:
    print(2**n)
elif odd==0 and p==1:
    print(0)
else:
    print(2**(n-1))
