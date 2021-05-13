import sys


for line in sys.stdin :
    if int(line.strip()) == 0 :
        break
    s = line.strip()
    sum = 0
    for c in s :
        sum += int(c)
    print(sum)

