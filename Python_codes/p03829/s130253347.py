n,a,b=map(int,input().split())
xs=list(map(int,input().split()))
l=[xs[i+1]-xs[i] for i in range(n-1)]
ans=[a*k if a*k < b else b for k in l]
print(sum(ans))