def modelAnswer(N:int) -> int:
   ans = 1
   for i in range(1,N+1):
      ans = (ans*i) % (10**9 + 7)
   return ans 
def main():
   N = int(input())
   print(modelAnswer(N))


if __name__ == '__main__':
   main()
