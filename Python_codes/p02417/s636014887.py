import sys
s = (sys.stdin.read()).lower()
for i in range(97,97+26):
    print('%s : %d' %(chr(i), s.count(chr(i))))