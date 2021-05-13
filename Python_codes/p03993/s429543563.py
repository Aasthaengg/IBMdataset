N=int(input())
a=list(map(int,input().split()))
I=[i for i in range (1,N+1)]
b=[]
for i in range(N):
    b.append([a[i],I[i]])
count=0
for i in range(N):
    if b[i][0]==b[b[i][0]-1][1] and b[i][1]==b[b[i][0]-1][0]:
        count+=1
print(count//2)