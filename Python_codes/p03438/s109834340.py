n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
if sum(A)>sum(B):
    ans='No'
else:
    c=0
    d=0
    for a,b in zip(A,B):
        if a<b:
            d+=(b-a)//2+(b-a)%2
            c+=(b-a)%2
        else:
            c+=a-b
    if d>=c:
        ans='Yes'
    else:
        ans='No'
print(ans)