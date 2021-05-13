import sys
def input(): return sys.stdin.readline().strip()
a,b,c=map(int,input().split())
if b-a==c-b:
    print('YES')
else:
    print('NO')