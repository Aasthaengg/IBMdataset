def main():
  s=str(input())
  l=len(s)
  f=None
  e=None
  for i in range(l):
    if s[i]=='A':
      f=i
      break
  for i in range(1,l):
    if s[-i]=='Z':
      e=l-i
      break
  print(e-f+1)
if __name__ == "__main__":
    main()