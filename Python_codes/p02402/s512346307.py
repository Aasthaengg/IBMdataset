n = int(input())
l =[int(i) for i in input().split()]

x = min(l)
y = max(l)
z = sum(l)

print('{} {} {}'.format(x,y,z))