

def myAnswer(N:int,B:list) -> None:
   ans = []
   for n,b in enumerate(B):
      if(n + 1 < b):
         print(-1)
         return
   
   while len(B) > 0:
      tmp = 0
      for n,b in enumerate(B):
         if(n + 1 == b):
            tmp = n
      ans.append(B[tmp])
      B.pop(tmp)
   for a in ans[::-1]:
      print(a)
   
def modelAnswer():
   return
def main():
   N = int(input())
   B = list(map(int,input().split()))
   myAnswer(N,B)
if __name__ == '__main__':
   main()