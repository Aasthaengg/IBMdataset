import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

K,A,B = MI()

if B-A <= 2 or K <= A-1:
    print(1+K)
else:
    K -= A-1
    print(A+(B-A)*(K//2) + K % 2)
