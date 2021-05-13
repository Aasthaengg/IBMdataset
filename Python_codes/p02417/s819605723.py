import sys
cnts = {chr(a):0 for a in range(ord('a'),ord('z')+1)}
for line in sys.stdin:
    alpha_line = [x.lower() for x in list(filter(lambda c: c.isalpha(), list(line)))]
    for a in alpha_line: cnts[a] += 1

for a in range(ord('a'),ord('z')+1): print(chr(a),':',cnts[chr(a)])