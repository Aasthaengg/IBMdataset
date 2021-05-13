import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

s = LS2()
a = ''.join(s[0:5])
b = ''.join(s[6:13])
c = ''.join(s[14:19])
print('{} {} {}'.format(a,b,c))
