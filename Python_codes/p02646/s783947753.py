A,V=map(int,input().split())
B,W=map(int,input().split())
T=int(input())

dist = abs(A-B)
v = V-W
if T*v>=dist:print('YES')
else:print('NO')