a,b,c=map(int,input().split())
n=len([i for i in range(1,c+1) if i%a==0])
print(b*n)
