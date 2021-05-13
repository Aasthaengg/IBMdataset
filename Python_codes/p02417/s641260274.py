import time
import sys
import io
import re
import math
#start = time.clock()
i = [0]*127
#n = raw_input()
for x in sys.stdin.read().lower():
    i[ord(x)]+=1
for y in range(ord('a'), ord('z')+1):
    print chr(y)+ ' : ' + str(i[y])