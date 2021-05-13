import sys;import math;print("\n".join(["{} {}".format(math.gcd(a,b), a // math.gcd(a,b) * b) for x in sys.stdin for a, b in [[int(y) for y in x.split()]] ]))
