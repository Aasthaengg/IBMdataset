def cin():
    in_ = list(map(int,input().split()))
    if len(in_) == 1:  return in_[0]
    else:  return in_

N = cin()
A = []
for i in range(N):
    in1, in2 = cin()
    A.append([in2, in1])

A = sorted(A)
t = 0
flg = 1
for i in range(N):
    t += A[i][1]
    if t > A[i][0]:  flg = 0
if flg:  print("Yes")
else:  print("No")