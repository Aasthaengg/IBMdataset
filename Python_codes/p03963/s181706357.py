import math
n,k=map(int,input().split()) #nボールk種類色
ans=k
for i in range(n-1):
    ans*=k-1
print(ans)