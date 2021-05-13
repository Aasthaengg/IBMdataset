def main():
  N = int(input())
  S = input()
  a = 0
  ans = ''
  
  for i in S:
    a = ord(i) + N 
    
    if (ord(i) + N) - ord('Z') > 0:
      a = (ord(i) + N) - 26
      
    ans += chr(a)
      
  print(ans)

  
  
main()