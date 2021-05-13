#abc082 a 
a,b=map(int,input().split())
ans=(a+b)//2+1
if a%2==b%2:
    ans-=1
print(ans)