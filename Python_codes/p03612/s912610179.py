
def myAnswer(N:int,P:list) -> int:
   ans = 0
   counter = 0
   for i in range(1,N+1):
      if(i == P[i - 1]):
         counter += 1
      elif(counter != 0):
         ans += counter//2 + counter % 2 if(counter > 1) else 1
         counter = 0
   if(counter != 0):
      ans += counter//2 + counter % 2 if(counter > 1) else 1
   return ans

def modelAnswer():
   return
def main():
   N = int(input())
   P = list(map(int,input().split()))
   print(myAnswer(N,P[:]))
if __name__ == '__main__':
   main()