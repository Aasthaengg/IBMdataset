N=int(input())
s=0
t=0
for i in range(N):
    a,b=input().split()
    if a<b:
        s+=3
    elif a==b:
        s+=1
        t+=1
    else:
        t+=3
print(t,s)
