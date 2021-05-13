n, a, b = map(int,input().split())
add = 0
if ( n % (a + b) ) < a :
    add = ( n % (a + b) ) % a
else:
    add = a
print((n // (a + b)) * a + add)