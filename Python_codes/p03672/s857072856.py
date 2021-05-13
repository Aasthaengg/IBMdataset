def main():
  s = input()
  if len(s)%2==0:
    s=s[:len(s)-2]
  else:
    s=s[:len(s)-1]
  while True:
    if(s[0:int(len(s)/2)]==s[int(len(s)/2):len(s)]):
      print(len(s))
      break
    s=s[:len(s)-2]

main()