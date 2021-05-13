#C
n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

t = [a,b,c,d,e]
t.sort()

if n % t[0] == 0:
    p = n // t[0]
else:
    p = n // t[0] + 1
    
print(4+p)