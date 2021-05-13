import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

import decimal
a,b,c = map(int, input().split())
val = (c-a-b)**2 - 4*a*b
if c-a-b<0:
    print("No")
else:
    if val>0:
        print("Yes")
    else:
        print("No")