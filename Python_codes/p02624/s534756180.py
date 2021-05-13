n=int(input())
print(sum(map(lambda x:n//x*(n//x+1)//2*x,range(1,n+1))))