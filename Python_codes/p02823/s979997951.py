N,A,B = map(int,input().split())
a = min(A,B)
b = max(A,B)
d = b - a

#差が偶数の時：d/2
#差が奇数の時：どちらかの端で一回稼ぐ

if d%2 == 0:
  print(d//2)
else:
  r = min(a,N-b+1)
  r += (b-a-1)//2
  print(r)