x, y = map(int, input().split())
import sys
if x%y == 0:
    print(-1)
    sys.exit()
for i in range(x,10**18,x):
    if i % y != 0:
        print(i)
        sys.exit()