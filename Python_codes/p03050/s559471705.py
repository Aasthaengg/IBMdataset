n=int(input())
ans=0
if n==1 or n==2:
    print(0)
    exit()

for i in range(n):
    if i**2>=n:
        x=i
        break

for i in range(1,x):
    if n%i==0:
        if n//i>i+1:
            ans+=n//i-1

print(ans)