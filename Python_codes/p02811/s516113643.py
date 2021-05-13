import math
import re
import copy
import sys

k,x = map(int,input().split())
if 500*k >= x:
    print('Yes')
else:
    print('No')