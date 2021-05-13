N=int(input())
K=int(input())
X=int(input())
Y=int(input())
if K<=N:
    result= (K * X )+ Y * (N-K)
else:
   result= N*X
print("% d"%result)