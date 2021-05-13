import sys
a = int(input())
if not ( 1 <= a <= 10 ): sys.exit()
if not isinstance(a,int): sys.exit()

print(a+a**2+a**3)