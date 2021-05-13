n=int(input())
a=list(map(int,input().split()))
a=sorted(a)

ans=0
for i in range(n):
    ans+=a[-i-1]*(-1)**(i)
    
    
print(ans)
