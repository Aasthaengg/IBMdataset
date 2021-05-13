a,b,k=map(int,input().split())
print(a-k,b) if a>=k else print(0,b-k+a) if k<=a+b else print(0,0)