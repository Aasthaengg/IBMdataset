k=int(input())
import sys
a,b=map(int,input().split())
for i in range(a,b+1):
    if i%k==0:
        print('OK')
        sys.exit()

print('NG')