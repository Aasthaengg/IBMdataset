a,b,c = map(int,input().split())
import sys
for i in  range(1,b+1):
    if ( a * i) % b == c:
        print('YES')
        sys.exit()
print('NO')