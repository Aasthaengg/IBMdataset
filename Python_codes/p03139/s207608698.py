n,a,b=map(int,input().split())
maxa = min(a,b)
mina = abs(min(0, n-(a+b)))
print(maxa,mina)