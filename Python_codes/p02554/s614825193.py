import math
from decimal import *
import random
from datetime import datetime
import time

mod = int(1e9)+7
n = int(input())
print(((10**(n))-(2*(9**n))+(8**n))%mod)
