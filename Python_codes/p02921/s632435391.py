def solve():
  s = input()
  t = input()
  ans = 0
  for i, j in zip(s, t):
    if i == j:
      ans += 1
  print(ans)
  return 0
 
if __name__ == "__main__":
  solve()
