
def myAnswer(N:int, K:int) -> int:
   return (K - 1)**(N - 1) * K

def modelAnswer():
   tmp=1
def main():
   N, K = map(int,input().split())
   print(myAnswer(N, K))
if __name__ == '__main__':
   main()