import sys
#input=sys.stdin.read
d=list(map(int, input().split()))
c=(d[0]+1)//2
if d[1] > c: print("NO")
else: print("YES")
