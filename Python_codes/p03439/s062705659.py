import sys
def main():
  N = int(input())
  
  print(0, flush = True)
  s = str(input())
  if s == "Vacant":sys.exit()
  l = [0, s]
  
  print((N-1), flush = True)
  r =  [N-1, str(input())]
  if r[1] == "Vacant":sys.exit()
  
  while True:
    print((l[0] + r[0])//2, flush = True)
    c = [(l[0] + r[0])//2, str(input())]
    if c[1] == "Vacant":sys.exit()
    if ((c[0]-l[0])%2 == 1 and c[1] == l[1]) or (c[0]-l[0])%2 == 0 and c[1] != l[1]:
      r = c
    else:
      l = c
          
if __name__ == "__main__":
  main()