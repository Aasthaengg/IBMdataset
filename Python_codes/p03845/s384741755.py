def solve():
  N = int(input())
  T = list(map(int, input().split()))
  M = int(input())
  ans = [sum(T)]*M
  for i in range(M):
    x,y = map(int, input().split())
    ans[i] += y-T[x-1]
  return ans
print(*solve(),sep='\n')