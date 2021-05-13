def solve():
  ans = 0
  N, Q = map(int, input().split())
  S = input()
  plus = [0]*N
  for i in range(1,N):
    plus[i] = plus[i-1]
    if S[i-1:i+1]=='AC':
      plus[i]+=1
  ans = [0]*Q
  for i in range(Q):
    x,y = map(int, input().split())
    ans[i] = plus[y-1]-plus[x-1]
  return ans
print(*solve(),sep='\n')