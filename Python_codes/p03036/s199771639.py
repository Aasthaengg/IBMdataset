def main():
  r,d,x = list(map(int,input().split()))
  for i in range(0,10):
    x=r*x-d
    print(x)
main()