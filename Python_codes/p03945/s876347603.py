def myAnswer(S:str) -> int:
   ans = 0
   pre = S[0]
   for s in S[1:]:
      if (pre != s):
         pre = s
         ans += 1
   return ans

def modelAnswer():
   return
def main():
   S = input()

   print(myAnswer(S))
if __name__ == '__main__':
   main()