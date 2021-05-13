def main():
  a,b = map(str,input().split())
  if a == 'H':
    ans = b
  else:
    if b == 'H':
      ans = 'D'
    else:
      ans = 'H'
  print(ans)
if __name__ == '__main__':
  main()