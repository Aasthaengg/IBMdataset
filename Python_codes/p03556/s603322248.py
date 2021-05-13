import math
def main():
  n = int(input())
  for i in reversed(range(1,n+1)):
    if math.sqrt(i) %1==0:
      print(i)
      break;
main()
