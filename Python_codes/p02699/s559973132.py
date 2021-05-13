import sys
input=lambda: sys.stdin.readline().rstrip()
s,w=map(int,input().split())
if w>=s:
  print("unsafe")
else:
  print("safe")