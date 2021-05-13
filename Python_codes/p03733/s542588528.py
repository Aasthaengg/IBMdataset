def myAnswer(N:int,T:int,t:list) -> int:
   total = T*N
   sub = 0
   if(N == 1): return T
   pre = t.pop(0)
   for time in t:
      if(pre + T - time > 0):
         sub += pre+T - time
      pre = time
   return total - sub

def modelAnswer():
   return
def main():
   N,T = map(int,input().split())
   t = list(map(int,input().split()))
   print(myAnswer(N,T,t[:]))
if __name__ == '__main__':
   main()