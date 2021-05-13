import sys
import string

count = {}

for key in list(string.ascii_lowercase):
    count[key] = 0

for line in sys.stdin:
    for case in line:
        case = case.lower()
        if count.get(case) != None:
            count[case] += 1

keys = list(count.keys())

keys.sort()
for key in keys:
    print ("%s : %s"%(key,count[key]))