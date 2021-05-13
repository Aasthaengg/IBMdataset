import sys
cnts = {}
for line in sys.stdin:
    alpha_line = [x.lower() for x in list(filter(lambda c: c.isalpha(), list(line)))]
    for c in alpha_line: 
        cnts[c] = cnts.get(c,0) + 1
 
for c in range(ord('a'),ord('z')+1): print(chr(c),':',cnts.get(chr(c),0))