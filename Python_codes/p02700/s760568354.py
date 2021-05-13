import sys
win = ''
def main():
  global win  
  a,b,c,d = list(map(int,(input().split())))
  while a > 0 and b > 0:
    c -=b
    if c <=0:
      win = 'Yes'
      break
    a -=d
    if a <=0:
      win = 'No'
      break
  print(win)    
  

if __name__ == '__main__':
  main()



