import fractions
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)
def myAnswer(N:int,M:int,S:str,T:str) -> int:
   a = N//fractions.gcd(N,M)
   b =M // fractions.gcd(N,M)
   # print(a,b)
   for i in range(fractions.gcd(N,M)):
      # print(S[a * i],T[b * i])
      if(S [a * i] != T[b * i]):
         return -1
   else:
      return lcm(N,M)

def modelAnswer():
   return
def main():
   N,M = map(int,input().split())
   S = input()
   T = input()
   print(myAnswer(N,M,S,T))
if __name__ == '__main__':
   main()
