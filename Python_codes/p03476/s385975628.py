q=int(input())
el=[True for _ in range(10**5+1)]
el[0]=False
el[1]=False
temp=[0]*(10**5+1)
i=2
while i*i<=10**5+1:
    for j in range(2*i,10**5+1,i): el[j]=False
    i+=1
cnt=0
for i,val in enumerate(el):
    if val and el[(i+1)//2]:
        cnt+=1
    temp[i]=cnt

for i in range(q):
    l,r=map(int,input().split())
    print(temp[r]-temp[l-1])