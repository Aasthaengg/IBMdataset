n=int(input())
A=[]
for i in range(n):
    A.append(int(input()))
l=1
ans=0
while l!=2 and ans<=n:
    l=A[l-1]
    ans+=1
print(ans if ans<=n else -1)