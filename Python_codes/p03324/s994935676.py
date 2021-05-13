def myAnswer(D:int, N:int) -> int:
   if(N == 100):
      return 100**D * (N + 1 )
   else:
      return 100**D * N


def modelAnswer():
   tmp=1
def main():
   D,N =map(int,input().split())
   print(myAnswer(D,N))
if __name__ == '__main__':
   main()