A,B,C=list(map(int, input().split()))
sum=A+B+C
max=max(A,B,C)
if sum%2==max%2:
  print((3*max-sum)//2)
else:
  print((3*(max+1)-sum)//2)