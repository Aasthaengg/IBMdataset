import sys
def S(): return sys.stdin.readline().rstrip()
N = S()
if all([n=='9' for n in N[1:]]):
    print(int(N[0])+9*(len(N)-1))
else:
    print(int(N[0])-1+9*(len(N)-1))
