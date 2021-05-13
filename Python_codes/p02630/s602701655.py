n=int(input())
a=list(map(int,input().split()))
q=int(input())
A=[0]*(10**5+1)
for i in a:
    A[i]+=1
a_sum=sum(a)
for j in range(q):
    b,c=map(int,input().split())
    x=(c-b)*A[b]
    a_sum+=x
    A[c]=A[c]+A[b]
    A[b]=0
    print(a_sum)