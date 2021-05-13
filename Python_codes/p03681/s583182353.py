import math
def myAnswer(N:int,M:int) -> int:
   if(abs(N - M) >= 2): return 0
   ans = 0
   if(abs(N - M) == 1):
      ans = math.factorial(N) * math.factorial(M)
   else:
      ans = math.factorial(N) ** 2 * 2

   return ans % (10**9 + 7)

def modelAnswer():
   return
def main():
   N,M = map(int,input().split())
   print(myAnswer(N,M))
if __name__ == '__main__':
   main()