a, b=map(int, input().split())
n=b-a-1
ans=(-a-b+n**2 +2*n+1)//2
print(ans)