n=int(input())
flag=0
k=1
while n>k*(k+1)//2:
    k+=1
ans=[]
while n!=0:
    if n-k>=0:
        n-=k
        ans.append(k)
    k-=1
ans.sort()
for x in ans:
    print(x)
