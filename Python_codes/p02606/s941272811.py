l,r,d = map(int,input().split())

x = -(-l//d)
y = r//d
print(y-x+1)