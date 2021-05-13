def myAnswer(N:int,s:str,t:str) -> int:
   if(s == t): return N
   if(N == 1): return 2
   total = N * 2
   # sとtを比較して重なった文字数をtotalから引く
   for i in range(N):
      if(s[i:] == t[:N-i]):
         total -= len(s[i:])
         break
   return total

def modelAnswer():
   return
def main():
   N = int(input())
   s = input()
   t = input()
   print(myAnswer(N,s,t))
if __name__ == '__main__':
   main()