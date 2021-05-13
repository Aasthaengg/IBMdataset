A,V=map(int,input().split())
B,W=map(int,input().split())
T=int(input())

diff_x=abs(A-B)
diff_a=max(V-W,0)

if T*diff_a>=diff_x:
  print('YES')
else:
  print('NO')