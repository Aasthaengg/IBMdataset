def myAnswer(D:int, N:int) -> int:
   if(D == 0):
      return 101 if(N == 100) else N
   elif(D == 1):
      return 10100 if(N == 100) else N*100
   else:
      return 1010000 if(N == 100) else N*10000
         



def modelAnswer():
   tmp=1
def main():
   D,N =map(int,input().split())
   print(myAnswer(D,N))
if __name__ == '__main__':
   main()
