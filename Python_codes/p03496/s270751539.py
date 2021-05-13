N=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
count=0
minus=0

for i in range(len(a)):
    if a[i]<0: minus+=1

if minus==0:
    for i in range(N-1):
        if a[i+1]-a[i]<0:
            a[i+1]+=a[i]
            b.append(i+1)
            c.append(i+2)
            count+=1
elif minus==len(a):
    for i in reversed(range(0,N-1)):
        if a[i+1]-a[i]<0:
            a[i]+=a[i+1]
            b.append(i+2)
            c.append(i+1)
            count+=1
else:
    count+=N
    if abs(max(a))>=abs(min(a)):
        ind=a.index(max(a))
        for i in range(N):
            b.append(ind+1)
            c.append(i+1)
        a2=list(map(lambda x:x+max(a),a))
        for i in range(N-1):
            if a2[i+1]-a2[i]<0:
                a2[i+1]+=a2[i]
                b.append(i+1)
                c.append(i+2)
                count+=1
    else:
        ind=a.index(min(a))
        for i in range(N):
            b.append(ind+1)
            c.append(i+1)
        a2=list(map(lambda x:x+min(a),a))
        for i in reversed(range(0,N-1)):
            if a2[i+1]-a2[i]<0:
                a2[i]+=a2[i+1]
                b.append(i+2)
                c.append(i+1)
                count+=1
print(count)
for i in range(len(b)):
    print(b[i]," ",c[i])