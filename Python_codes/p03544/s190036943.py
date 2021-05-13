n=int(input())
if n==0:
    print(2)
    exit()
elif n==1:
    print(1)
    exit()
else:
    nu1=2
    nu2=1
    for i in range(n-1):
        nu3=nu1+nu2
        nu1=nu2
        nu2=nu3
print(nu3)