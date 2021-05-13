import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

s = LS2()
s[5] = ' '
s[13] = ' '
print(''.join(s))
