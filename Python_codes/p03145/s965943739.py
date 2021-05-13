a, b, c = [int(i) for i in input().split()]
if a >= b and a >= c:
 print(c*b//2)
elif b >= c and b >= a:
 print(a*c//2)
else:
 print(a*b//2)
