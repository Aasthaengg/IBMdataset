def myAnswer(N:int,A:list) -> int:
   counter = 0
   for i in range(N):
      if(A[A[i]-1] == i + 1):
         counter += 1
   return counter//2


def modelAnswer():
   tmp=1
def main():
   N = int(input())
   A = list(map(int,input().split()))
   print(myAnswer(N,A[:]))
if __name__ == '__main__':
   main()