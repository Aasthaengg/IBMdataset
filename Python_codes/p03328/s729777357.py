a,b=(int(i) for i in input().strip().split(" "))
n=b-a
k=(n*(n+1))//2
print(k-b)