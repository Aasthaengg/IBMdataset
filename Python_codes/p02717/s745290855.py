a,b,c = map(int, input().split())
t = a
a = b
b = t

u = a
a = c
c = u

print(str(a)+' '+str(b)+ ' '+str(c))