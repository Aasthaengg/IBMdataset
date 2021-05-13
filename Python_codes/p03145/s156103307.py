a,b,c = map(int, input().split())

import math
s = (a+b+c)/2
S = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(int(S))