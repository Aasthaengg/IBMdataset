a=[]
a=input().split(" ")
N=int(a[0])
A=int(a[1])
B=int(a[2])
b=[]
for c in range(0,N):
    c=input().split(" ")
    b.extend(c)
#bの偶数がAi,bの奇数がBi
d=0
for i in range(0,N):
    b1=int(b[2*i])
    b2=int(b[2*i+1])

    if b1 >= A and b2 >= B :
        d=d+1
    else:
        continue
print(d)
