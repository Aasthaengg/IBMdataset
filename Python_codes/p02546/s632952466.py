def main():
  s = input()
  if s[-1] == 's':
    ans = s + 'es'
  else:
    ans = s + 's'
  print(ans)
  
main()
