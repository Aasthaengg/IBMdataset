a,b,x = map(int, input().split())

s = (a-1)//x
if a == 0: s = -1
p = b//x

print(p - s)