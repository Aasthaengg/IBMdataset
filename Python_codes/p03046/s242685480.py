m,k=map(int,input().split())
r=range(2**m)
if k:a=[i for i in r if i!=k];print(*[-1]*(m==k==1or k>=2**m)or[k]+a+[k]+a[::-1])
else:[print(i,i)for i in r]