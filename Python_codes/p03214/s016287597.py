N=int(input())
a=list(map(int,input().split()))
b=0
for i in range(len(a)):
    b+=a[i]
b=b/len(a)
c=[]
for i in range(len(a)):
    c.append(abs(a[i]-b))
for i in range(len(c)):
    if c[i]==min(c):
        print(i)
        break