n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
a,b=max(l)
print(a+b)