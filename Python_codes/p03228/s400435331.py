
a,b,k=map(int,input().split())
#n=int(input())
#for i in range(n):
#    p[i]=[int(input()),i]
t=0
for i in range(k):
    if t==0:
        if a%2==0:
            a,b=(a)//2,b+(a)//2
        else:
            a,b=(a-1)//2,b+(a-1)//2
    if t==1:
        if b%2==0:
            b,a=(b)//2,a+(b)//2
        else:
            b,a=(b-1)//2,a+(b-1)//2
    t=1-t
print(a,b)