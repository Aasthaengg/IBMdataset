n,p = map(int,input().split())
a = list(map(int,input().split()))
odd = 0
even = 0
for ai in a:
    if(ai%2==0):
        even += 1
    else:
        odd += 1

if(p==1)&(odd==0):
    print(0)
elif(p==0)&(odd==0):
    print(2**n)
else:
    print(2**(n-1))
