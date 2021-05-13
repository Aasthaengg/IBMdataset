
from re import search
def myAnswer(N:int,A:int,B:int,C:int,D:int,S:str) -> str:
   if (search(r'##',S[A-1:max(C,D)])): return "No"
   if(C > D):
      return "Yes" if (search(r'\.\.\.',S[B - 2:D+1])) else "No"
   return "Yes"

def modelAnswer():
   return
def main():
   N,A,B,C,D = map(int,input().split())
   S = input()
   print(myAnswer(N,A,B,C,D,S))
if __name__ == '__main__':
   main()