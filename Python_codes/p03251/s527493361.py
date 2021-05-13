import sys
N,M,X,Y = map(int,input().split())
array_x = list(map(int,input().split()))
array_y = list(map(int,input().split()))

if not ( 1 <= N <= 100 and 1 <= M <= 100 ): sys.exit()
if not ( -100 <= X <= 100 and -100 <= Y <= 100 ): sys.exit()
for I in array_x:
    if not ( -100 <= I <= 100 and array_x.count(I) == 1 and I != X): sys.exit()
for J in array_y:
    if not ( -100 <= J <= 100 and array_y.count(J) == 1 and J != Y): sys.exit()

for I in range(X+1,Y+1):
    if I > max(array_x) and I <= min(array_y):
        print('No War')
        sys.exit()
print('War')