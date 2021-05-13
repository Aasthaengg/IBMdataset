import math
from decimal import *
import random

a,b,c,d = map(int, input().split())
print(max(a*c,
          a*d,
          b*c,
          b*d))
