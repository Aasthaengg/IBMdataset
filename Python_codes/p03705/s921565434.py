import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
N,A,B = LI()
if A>B:
    print(0)
    exit()
if N==1:
    print(1 if A==B else 0)
    exit()
print((N-2)*(B-A)+1)
