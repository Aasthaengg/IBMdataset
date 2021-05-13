def myAnswer(S:str) -> str:
   N = len(S) - 7
   for i in range(N,len(S)):
      # print(S[:i-N],S[i:])
      if(S[:i-N]+S[i:] == "keyence"):
         return "YES"
   return "NO"



def modelAnswer():
   return
def main():
   S = (input())
   print(myAnswer(S))
if __name__ == '__main__':
   main()