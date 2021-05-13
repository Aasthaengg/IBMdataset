from math import factorial
def myAnswer(N:int) ->int:
   ans =factorial(N)
   return ans % (10**9 + 7)

def modelAnswer():
   tmp=1
def main():
   N = int(input())
   print(myAnswer(N))


if __name__ == '__main__':
   main()