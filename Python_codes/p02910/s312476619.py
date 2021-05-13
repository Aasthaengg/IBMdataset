def main():
  s=input()
  flg=0
  for i in range(0,len(s)):
    if i%2==1:
      if s[i]=='R':
        flg=1
        break
    else:
      if s[i]=='L':
        flg=1
        break
  if(flg==1):
    print('No')
  else:
    print('Yes')
    
main()