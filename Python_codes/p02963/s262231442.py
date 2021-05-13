s = int(input())
x = [0,10**9]
y = [0,1]
tmp = 10**9
x3 = 0
if s % tmp != 0:
    x3 = tmp - (s % tmp)

y3 = (s + x3) // tmp

print(0,0,10**9,1,x3,y3)
