n=int(input())
v=list(map(int, input().split()))
even=[0]*(10**6 + 1)
odd=[0]*(10**6 + 1)



for i in range(n):
    if i%2==0:
        even[v[i]]+=1
    else:
        odd[v[i]]+=1

a=max(even)
M=even.index(a)
even[M]=0
a_second=max(even)
even[M]=a

b=max(odd)
N=odd.index(b)
odd[N]=0
b_second=max(odd)
odd[N]=b


if M!=N:
    ans=sum(even)-a + sum(odd)-b
    print(ans)
else:
    ans=min(sum(even)-a + sum(odd)-b_second, sum(even)-a_second + sum(odd)-b)
    print(ans)