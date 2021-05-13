N=int(input())
K=int(input())
X=int(input())
Y=int(input())
if (N>K):
  sum=K*X+(N-K)*Y
  print(sum)
else:
  sum=N*X
  print(sum)