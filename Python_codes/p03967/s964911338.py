def main():
  s = str(input())
  p = 0
  for i in range(len(s)):
    if s[i] == 'p':
      p += 1
  print(len(s)//2-p)
  
if __name__ == "__main__":
  main()