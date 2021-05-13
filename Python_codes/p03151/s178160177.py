N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

m=0
c=0
for i in range(N):
    if B[i]>A[i]:
        m+=B[i]-A[i]
        c+=1

li=[]
for i in range(N):
    if B[i]<A[i]:
        li.append(A[i]-B[i])
li.sort(reverse=True)
for k in li:
    if m==0:
        break
    m-=min(m,k)
    c+=1
print(c if m==0 else -1)