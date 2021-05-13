import sys
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし

N = LI2()
print('Yes' if N[0] == N[-1] else 'No')