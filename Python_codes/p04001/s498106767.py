
def equa(ans,i,s,p):
  for e in (0,1):
    p[i] = e
    if i < len(p)-2:
      ans = equa(ans,i+1,s,p)
    else:
      #print(i,s,p)
      prii = 0
      for ii in range(len(p)):
        if p[ii] == 1:
          ans += int(s[prii:ii+1])
          #print(prii,ii+1,int(s[prii:ii+1]))
          prii = ii+1
  return ans
def main():
  s = input()
  p = [0]*(len(s)-1)
  p.append(1)
  i = 0
  ans = 0
  ans = equa(ans,i,s,p)
  print(ans)
  
if __name__ == '__main__':
  main()