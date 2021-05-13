import sys
input=lambda: sys.stdin.readline().rstrip()
a,b,c=map(int,input().split())
k=int(input())
ct=0
while b<=a:
  ct+=1
  b*=2
while c<=b:
  ct+=1
  c*=2
if ct<=k:
  print("Yes")
else:
  print("No")