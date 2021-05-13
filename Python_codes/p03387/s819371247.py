A,B,C=map(int,input().split())
M=max(A,B,C)
tmp=M*3
Sum=A+B+C
Check=tmp-Sum
if Check%2==0:
  ans=(tmp-Sum)//2
else:
  tmp2=(M+1)*3
  ans=(tmp2-Sum)//2
print(ans)