import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

A = LI()
A.sort()

if A[0]+A[1] == A[2]:
    print('Yes')
else:
    print('No')