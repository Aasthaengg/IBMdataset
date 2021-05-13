a,b = map(int,input().split())
n = b-a
tower = ((n+1)*n)/2
print(int(tower-b))
