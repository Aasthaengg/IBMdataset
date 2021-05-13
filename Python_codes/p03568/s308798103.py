def myAnswer(N:int,A:list) -> int:
   counter = 0
   for a in A:
      if(a % 2==0):
         counter +=1

   return 3**N-2**counter






def modelAnswer():
   tmp=1
def main():
   N = int(input())
   A = list(map(int,input().split()))
   print(myAnswer(N,A[:]))
if __name__ == '__main__':
   main()