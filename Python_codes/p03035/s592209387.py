import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


A,B = MI()
if A <= 5:
    print(0)
elif A >= 13:
    print(B)
else:
    print(B//2)
