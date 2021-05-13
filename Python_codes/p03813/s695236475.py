import sys

rate = int(input())
if rate < 0 or rate > 3000:
    sys.exit()

if rate < 1200:
    print("ABC")
else:
    print("ARC")