n,a,b=map(int,input().split())
print(a if a<b else b,end=" ")
print(a+b-n if a+b-n>0 else 0)
