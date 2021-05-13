import sys
from collections import OrderedDict
AZC = OrderedDict((chr(i), 0) for i in range(97,97+26))

import fileinput
for line in fileinput.input():
 S = line.strip().lower()
 for i in S:
  if i in AZC:
   AZC[i] += 1

for  s, n in AZC.items():
 print(s + " : " + str(n)) 