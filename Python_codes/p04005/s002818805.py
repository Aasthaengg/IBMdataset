A,B,C = map(int,input().split())
mini = 10**27
if A%2 == 0 or B%2 ==0 or C%2 ==0:
  mini = 0
  ans =0
else:
  x = int(A/2)
  ans1 = (x+1)*B*C-x*B*C 
  y = int(B/2)
  ans2 = (y+1)*A*C - y*A*C
  z = int(C/2)
  ans3 = (z+1)*B*A - z*B*A

  ans = min([ans1,ans2,ans3])
print(ans)
