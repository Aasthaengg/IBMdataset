N = int(input())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))
ans = 0
for i in range(N):
  tmp = sum(A1[0:i+1])
  tmp = tmp + sum(A2[i:N])
  ans = max(ans,tmp)
print(str(ans))