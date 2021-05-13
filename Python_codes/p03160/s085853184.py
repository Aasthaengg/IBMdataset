inf = 10**9

def main():
  N = int(input())
  h = list(map(int,input().split()))
  memo = [inf]*N
  memo[0] = 0
  
  def calcCost(start,goal,h):
    return abs(h[goal]-h[start])
  
  for i in range(1,N):
    memo[i] = min(memo[i],memo[i-1]+calcCost(i-1,i,h))
    if i > 1:
      memo[i] = min(memo[i],memo[i-2]+calcCost(i-2,i,h))
  print(memo[-1])

main()