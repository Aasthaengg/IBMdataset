a=[]
n=int(input())
m=n
if n%2==0:
    m+=1
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if i+j!=m:
            b=(i,j)
            a.append(b)
print(len(a))
for i in a:
    print(str(i[0])+" "+str(i[1]))