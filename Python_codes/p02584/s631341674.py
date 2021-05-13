x,k,d=map(int, input().split())
x=abs(x)

if x+d >=k*d:
    print(abs(x-k*d))
    exit()

if k%2==1:
    x=x-d

kaisu=int(x/(2*d))
ans=abs(x-kaisu*d*2)
if ans >=d:
    ans=2*d-ans

print(ans)