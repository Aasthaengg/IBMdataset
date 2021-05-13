def main():
  h,w = list(map(int,input().split()))
  a = [input() for i in range(h)]
  
  for i in range(0,w+2):
    print("#",end="")
  print()
  for i in range(0,h):
    print("#"+a[i]+"#")
  for i in range(0,w+2):
    print("#",end="")
    
main()