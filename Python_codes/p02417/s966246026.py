import sys
letters = 'abcdefghijklmnopqrstuvwxyz'
s = sys.stdin.read().lower()
for i in range(26) :
    print(letters[i] + ' : %d' % s.count(letters[i]))
