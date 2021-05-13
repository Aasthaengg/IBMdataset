a,b,t=[int(x) for x in input().split()]
x=2
total=a
biscoito=0
while total<=(t+0.5):
    biscoito+=b
    total=x*a
    x+=1
print(biscoito)