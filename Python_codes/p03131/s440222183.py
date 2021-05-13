def myAnswer(K:int,A:int,B:int) -> int:
   if((B - A) <=2):
      return K + 1
   else:
      return max(0,(K - (A - 1)) // 2)*(B - A) + A + (K - (A - 1)) % 2


def modelAnswer():
   return
def main():
   K,A,B = map(int,input().split())
   print(myAnswer(K,A,B))
if __name__ == '__main__':
   main()