
def myAnswer(N:int,s:str,t:str) -> int:
   if(s == t): return N
   if(N == 1): return 2
   total = N * 2
   for i in range(N):
      counter = 0
      n = i
      for j in range(N-i):
         # print(s[n],t[j])
         if(s[n] == t[j]):
            n += 1
            counter += 1
         else:
            break
      else:
         total -= counter
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