import sys
K,X = map(int,input().split())

if not ( 1 <= K <= 100 and 0 <= X <= 100 ): sys.exit()

for I in range(X-K+1,X+K):
    print(I)