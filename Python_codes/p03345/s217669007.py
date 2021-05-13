a,b,c,k=map(int,input().split())

lim=10**18
if k%2==0:
    print(a-b if a-b<=lim else "unfair")
elif k%2==1:
    print(b-a if b-a<=lim else "unfair")
