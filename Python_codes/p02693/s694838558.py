import sys
K = int(input())
A,B = map(int,input().split())

if not ( 1 <= K <= 1000 ): sys.exit()
if not ( 1 <= A <= 1000 and A <= B <= 1000 ): sys.exit()

for I in range(A,B+1):
    if I % K == 0:
        print('OK')
        sys.exit()
print('NG')