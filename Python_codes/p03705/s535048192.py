def myAnswer(N:int,A:int,B:int) -> int:
   if((N== 1 and  A != B )or B - A < 0): return 0
   ans = (B*(N-1) + A) - (A * (N - 1) + B) + 1
   return ans

def modelAnswer():
   return
def main():
   N,A,B = map(int,input().split())
   print(myAnswer(N,A,B))
if __name__ == '__main__':
   main()