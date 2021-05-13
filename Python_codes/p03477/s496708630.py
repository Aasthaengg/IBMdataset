import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

A,B,C,D = MI()
if A+B > C+D:
    print('Left')
elif A+B < C+D:
    print('Right')
else:
    print('Balanced')
