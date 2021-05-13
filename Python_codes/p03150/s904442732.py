def myAnswer(S:str) -> str:
   if(S == "keyence"):return "YES"
   for i in range(len(S)-1):
      for j in range(i+1,len(S)):
         if(S[:i]+S[j:] == "keyence"):
            return "YES"
   return "NO"

def modelAnswer():
   return
def main():
   S = (input())
   print(myAnswer(S))
if __name__ == '__main__':
   main()