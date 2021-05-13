def myAnswer(S:str)-> str:
   N = len(S)
   if(N == 1): return "YES"
   dic = {"a":0,"b":0,"c":0}
   for s in S:
      dic[s] += 1
   # print(dic)
   dic = list(dic.values())
   dic.sort(reverse = True)
   first = dic.pop(0)
   seccond = dic.pop(0)
   third = dic.pop(0)
   if(first - third <= 1):
      return "YES"
   else:
      return "NO"




def modelAnswer():
   return
def main():
   S = (input())
   print(myAnswer(S))
if __name__ == '__main__':
   main()