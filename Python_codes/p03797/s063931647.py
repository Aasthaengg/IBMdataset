n,m=map(int,input().split())
ans=n+(m-2*n)//4 if m-2*n>=0 else m//2
print(ans)