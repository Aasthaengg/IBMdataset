def solve():
  k, x = map(int, input().split())
  if x-k+1 < -1000000:
    ans = list(range(-1000000,x))+list(range(x,x+k))
  elif x+k-1 > 1000000:
    ans = list(range(x-k+1,x))+list(range(x,1000000))
  else:
    ans = list(range(x-k+1,x))+list(range(x,x+k))
  ans = map(str, ans)
  print(" ".join(ans))
  return 0
 
if __name__ == "__main__":
  solve()
