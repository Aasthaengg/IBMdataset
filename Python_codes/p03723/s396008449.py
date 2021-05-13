def main():
  a,b,c = map(int,input().split())
  s = [a,b,c]

  cnt = 0
  while (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0):
    
    a1,b1,c1 = a,b,c
    a = (b1+c1)//2
    b = (a1+c1)//2
    c = (a1+b1)//2
    
    if [a,b,c] == s:
      return -1
    
    cnt += 1
    #print(a,b,c)
    
  return cnt    
    

ans = main()
print(ans)