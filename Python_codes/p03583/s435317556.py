def main():
  N=int(input())
  for h in range(1,3501):
    for n in range(1,3501):
      if 4*h*n>N*(h+n) and (N*h*n)%(4*h*n-N*(h+n))==0:
        print(h,n,(N*h*n)//(4*h*n-N*(h+n)))
        return
main()