N=int(input())
a=0
b=[]
for i in range(N):
    b.append(0)
for i in range(1,N+1):
    for j in range(1,i+1):
        if i%j==0 and i%2==1:
            b[i-1]+=1
print(b.count(8))