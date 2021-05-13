n=int(input())
v=list(map(int,input().split()))

odd=[0]*(10**5+1)
even=[0]*(10**5+1)
for i in range(0,n,2):
    odd[v[i]]+=1
for i in range(1,n+1,2):
    even[v[i]]+=1

odd_mx=0
odd_sec=0
even_mx=0
even_sec=0
for i in range(len(odd)):
    if odd[i]>odd_mx:
        odd_sec=odd_mx
        odd_mx=odd[i]
        odd_idx=i
    elif odd[i]>odd_sec:
        odd_sec=odd[i]
for i in range(len(even)):
    if even[i]>even_mx:
        even_sec=even_mx
        even_mx=even[i]
        even_idx=i
    elif even[i]>even_sec:
        even_sec=even[i]

if odd_idx!=even_idx:
    ans=n-(odd_mx+even_mx)
elif odd_mx==even_mx and odd_sec==0 and even_sec==0:
    ans=n//2
else:
    a=max(even_mx+odd_sec,odd_mx+even_sec)
    ans=n-a

print(ans)