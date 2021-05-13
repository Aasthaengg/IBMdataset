#
import sys
import math
import numpy as np
import itertools
# ひとつ入力
n = int(input())
answer = 0
while n>0:
    if n%10==2:
        answer += 1
    n = n // 10
print(answer)
