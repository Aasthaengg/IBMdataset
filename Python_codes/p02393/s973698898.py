x = input().split()

for i in range(len(x)):
    x[i] =int(x[i])

a,b,c=x
while a> b or b > c or a > c:
    if a > b:
        a,b = b,a
    if b > c:
        b,c = c,b
    if a>c:
        a,c=c,a
print(a,b,c)

