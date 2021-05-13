n,a,b=map(int,input().split())
n-=2;print(max(b*n-a*n+1,0))