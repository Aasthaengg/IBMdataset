n,m=map(int, input().split())
x=min(n, m//2)
print(x+(m-x*2)//4)