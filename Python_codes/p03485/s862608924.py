s = input().split()
p = [int(w) for w in s]

a = p[0]
b = p[1]

c = ( a + b ) % 2

if(c == 0):
    print(   int((a+b)/2)    )
else:
    print(   int((a+b+1)/2)    )