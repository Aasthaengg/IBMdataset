# solution

import io
import sys
import math

nim, mike = map(int, input().split())

if mike==0:
    print(nim*nim)
    exit()

b = mike+1

counter = 0

while b<=nim:
    counter += (nim//b)*(b-mike)+max(nim%b-mike+1, 0)
    b += 1

print(counter)