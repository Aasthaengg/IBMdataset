import sys
N,i = map(int,input().split())
if not ( 1 <= N <= 100 and 1 <= i <= N ):
    sys.exit()

print(N - i + 1)