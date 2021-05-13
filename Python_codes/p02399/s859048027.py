a,b = map(int, raw_input().split())

x = a/b
y = a%b
z = float(a)/float(b)
z = round(z,8)

print '%d %d %.8f' %(x,y,z)