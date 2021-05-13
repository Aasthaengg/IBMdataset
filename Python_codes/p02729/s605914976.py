def main():
  m, n = map(int, input().split())
  
  if n <= 1:
    ans1 = 0
  else:
    ans1 = n * (n-1) / 2
    
  if m <= 1:
    ans2 = 0
  else:
    ans2 = m * (m-1) / 2
    
  print(int(ans1 + ans2))
  
main()