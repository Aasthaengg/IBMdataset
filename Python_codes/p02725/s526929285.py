K,N = map(int,input().split())
array = list(map(int,input().split()))
ans = 10**8
for i in range(N):
  if i == 0:
    ans1 = array[-1] - array[i]
  else:
    ans1 = array[i-1] + ( K - array[i] )
  if i == N-1:
    ans2 = array[-1] - array[0]
  else:
    ans2 = array[i] + ( K - array[i+1] )
  ans = min(ans,ans1,ans2)
print(ans)