def main():
  s = input()
  p = len(s)
  i = 0
  ans = 0
  for i in range(2 ** (p-1)):
    t = s[0]
    for j in range(0,p-1):
      if (i & (1 << j)):
        t = t + "+"
      t = t + s[j+1]
      
    #print(bin(i),t,eval(t))
    ans += eval(t)
    
  print(ans)
  
if __name__ == '__main__':
  main()