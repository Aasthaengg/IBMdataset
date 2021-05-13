x,y = map(int,input().split())
import fractions
g = fractions.gcd(x,y)
if x == y:
    print(-1)
elif y == 1:
    print(-1)
elif x > y and y == g:
    print(-1)
elif x < y:
    print(x)
elif x % y == 0:
    print(-1)
else:
    print(x)