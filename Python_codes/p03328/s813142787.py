a,b=map(int,input().split())
x=[int(i) for i in range(1,1000)]
print(sum(x[:(b-a-1)])-a)
