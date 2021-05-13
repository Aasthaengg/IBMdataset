import sys

alnum = ord('z') - ord('a') + 1
res = [0] * alnum

for line in sys.stdin:
    instr = line.lower()

    for s in instr:
        if s.isalpha():
            relc = ord(s) - ord('a')
            res[relc] += 1

for i in range(alnum):
    print("{0} : {1}".format(chr(i + ord('a')), res[i]))

