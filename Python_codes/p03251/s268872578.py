n,m,x,y=map(int,input().split())
a=[int(_) for _ in input().split()]
b=[int(_) for _ in input().split()]
print('War' if x>=min(b) or max(a)>=y or max(a)>=min(b) else 'No War')