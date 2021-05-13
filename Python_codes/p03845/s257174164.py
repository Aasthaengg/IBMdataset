def solve() : 
  time = list()
  
  N = int(input())
  
  time = list(map(int, input().split()))
  
  M = int(input())
  
  for i in range(M) : 
    p, x = tuple(map(int, input().split()))
    
    ans = time.copy()
    ans[p - 1] = x
    sum = 0
    for j in range(len(ans)) :
      sum += ans[j]
    print(sum)
    
solve()