import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

S = LS2()
a = S.count('+')
b = S.count('-')
print(a-b)