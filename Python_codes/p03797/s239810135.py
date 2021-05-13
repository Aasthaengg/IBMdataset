
n,m=map(int,input().split())
first=min(n,m//2)
n -=first
m-=first*2
second = m//4
print(second+first)