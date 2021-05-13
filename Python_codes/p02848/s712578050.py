def main():
  n=int(input())
  s=input()
  ans=""
  for i in range(0,len(s)):
    ans+=chr(((ord(s[i])-ord('A')+n)%26)+ord('A'))
  print(ans)

main()