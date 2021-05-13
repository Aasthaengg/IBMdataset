from collections import defaultdict
def solve():
  H, W, N = map(int, input().split())
  ans = [0]*10
  dic = defaultdict(lambda: defaultdict(lambda: 0))
  for i in range(N):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(x-1,x+2):
      for j in range(y-1,y+2):
        if i>0 and i<H-1 and j>0 and j<W-1:
          if dic[i][j]>0:
            ans[dic[i][j]] -= 1
          dic[i][j] += 1
          ans[dic[i][j]] += 1
  total = (H-2)*(W-2)
  ans[0] = total - sum(ans[1:])
  return ans
print(*solve(),sep='\n')