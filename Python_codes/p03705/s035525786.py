n,a,b = map(int,input().split())

if n==1 and a!=b: print(0)
elif n==1 and a==b: print(1)
elif n>=2 and a>b: print(0)
elif n>=2 and a==b: print(1)
elif n>=2 and a<b: print(b*(n-2) - a*(n-2) + 1)