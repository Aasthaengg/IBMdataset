n=int(input())
a=list(map(int,input().split()))
ans=sum(a)
a=list(map(lambda x: 2*x,a))
odd=0
for i in a[1::2]: odd+=i
k1=ans-odd
print(k1,end=" ")
for i in a[:n-1]:
    k1=i-k1
    print(k1,end=" ")