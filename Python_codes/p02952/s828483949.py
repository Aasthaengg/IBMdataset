n=int(input())
t=n
c=1
while t>=10:
    t=t//10
    c=c+1
ans=0
for i in range(1,c):
    if i%2==1:
        ans+=10**(i)-10**(i-1)
if c%2==1:
    ans=ans+n+1-10**(c-1)
print(ans)