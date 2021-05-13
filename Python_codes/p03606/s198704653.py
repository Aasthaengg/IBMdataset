def sumnumber(N) : 
  sum = 0
  for i in range(N) : 
    l , r = tuple(map(int, input().split()))
    sum += (r - l) + 1
    
  return sum


N = int(input())

print(sumnumber(N))
