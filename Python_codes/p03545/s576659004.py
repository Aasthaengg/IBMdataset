import sys

s = input()

for i in range(2**3):
    localsum = s[0]
    for j in range(3):
        if (i >> j) & 1:
            localsum += "+"
        else:
            localsum += "-"
        localsum += s[j+1]
    sum = eval(localsum)
    if sum == 7:
        localsum += "=7"
        print(localsum)
        sys.exit()