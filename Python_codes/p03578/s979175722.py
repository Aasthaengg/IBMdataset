
def myAnswer(N:int,D:list,M:int,T:list) -> str:
   dic = {key:0 for key in T}
   for d in D:
      if(d in dic.keys()):
         dic[d] += 1
   for t in T:
      if(dic[t] == 0):
         return "NO"
      else:
         dic[t] -= 1
   return "YES"

def modelAnswer():
   return
def main():
   N = int(input())
   D = list(map(int,input().split()))
   M = int(input())
   T = list(map(int,input().split()))
   print(myAnswer(N,D[:],M,T[:]))
if __name__ == '__main__':
   main()