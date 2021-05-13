'''
Accepted    　:No
difficult   　: 
ペナルティ　  　:5分
実際の回答時間  :分
WAの回数　     :回
合計時間　　  　:分
'''
import collections
def myAnswer(N:int,V:list) -> int:
   odd = []
   even = []
   if len(set(V)) == 1:
      return N//2

   for n,v in enumerate(V):
      even.append(v) if n % 2 == 0 else odd.append(v)
   
   oddCounter = collections.Counter(odd)
   evenCounter = collections.Counter(even)
   oddCounter = sorted(oddCounter.items(),key=lambda x:x[1])
   evenCounter = sorted(evenCounter.items(),key=lambda x:x[1])
   oddMAX = oddCounter[-1][0]
   evenMAX = evenCounter[-1][0]
   if oddMAX == evenMAX:
      evenLen = len(evenCounter)
      oddLen = len(oddCounter)
      if evenLen >= 2 and oddLen >= 2:
         if evenCounter[-2][1] > oddCounter[-2][1]:
            evenMAX = evenCounter[-2][0]
         else:
            oddMAX = oddCounter[-2][0]
      elif evenLen >= 2:
         evenMAX = evenCounter[-2][0]
      else:
         oddMAX = oddCounter[-2][0]

   
   total = 0
   for n,v in enumerate(V):
      if n % 2 == 1:
         if oddMAX != v:
            total += 1
      else:
         if evenMAX != v:
            total += 1
   return total
def modelAnswer():
   return
def main():
   N = int(input())
   V = list(map(int,input().split()))
   print(myAnswer(N,V))


if __name__ == '__main__':
   main()
