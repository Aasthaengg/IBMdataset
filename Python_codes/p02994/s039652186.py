import math
import datetime
from math import fabs
def main():
    inp,var = map(int, input().split())
    var3 = [var+i-1 for i in range(1,inp+1)]
    var2 = min(var3, key=abs)
    x=sum(var3)-var2
    return x
print(main())