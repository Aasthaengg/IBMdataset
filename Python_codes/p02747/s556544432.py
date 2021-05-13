def main():
  S = input()
  lst = []
  for i in range(1, 100):
    lst.append('hi' * i)

  for it in lst:
    if S == it:
      print('Yes')
      return

  print('No')
  
if __name__ == '__main__':
  main()