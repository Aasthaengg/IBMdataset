def myAnswer(N:int,C:int,K:int,T:list)->int:
   T.sort()
   ans = 0
   counter = 1
   hantei = T.pop(0)
   for t in T:
      if(counter == C or (t - hantei) > K):
         ans += 1
         hantei = t
         counter = 1
      else:
         counter += 1
   ans += 1
   return ans

def modelAnswer():
   return
def main():
   N,C,K = map(int,input().split())
   T = [int(input()) for _ in range(N)]
   print(myAnswer(N,C,K,T))

if __name__ == '__main__':
   main()