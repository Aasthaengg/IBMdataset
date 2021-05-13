n,m=map(int,input().split())
if n>m: m,n=n,m
print(m-2 if n==1 and m>1 else 1 if n==1 else (n-2)*(m-2))
#四隅は4回,その他の端は6回,その他は9回ひっくり返るので(n-2)*(m-2)