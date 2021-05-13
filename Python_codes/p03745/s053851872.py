N=int(input())
A=list(map(int,input().split()))
sw="1"
ans=1

for i in range(N-1):
    if sw=="1":
        if A[i]>A[i+1]:
            sw="2"
        if A[i]<A[i+1]:
            sw="3"
    elif sw=="2":
        if A[i]<A[i+1]:
            ans+=1
            sw="1"
    elif sw=="3":
        if A[i]>A[i+1]:
            ans+=1
            sw="1"

print(ans)
