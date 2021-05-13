def myAnswer(N:int,M:int) -> int:
   ans = (1900 * M + (N - M) * 100) * 2 ** M
   return ans

def modelAnswer():
   return
def main():
   N,M = map(int,input().split())
   print(myAnswer(N,M))
if __name__ == '__main__':
   main()