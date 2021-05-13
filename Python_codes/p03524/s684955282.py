
def myAnswer(S:str)-> str:
   #len(S)が2の時種類数が１以外ならOK
   dic = {"a":0,"b":0,"c":0}
   for s in S:
      dic[s]+= 1
   # print(dic)
   dic2 = sorted(dic.values(),reverse = True)
   sub = dic2[0] - dic2[1] + dic2[1] - dic2[2]
   # print(dic2)
   if(sub >=2):
      return "NO"
   else:
      return "YES"
def modelAnswer():
   return
def main():
   S = (input())
   print(myAnswer(S))
if __name__ == '__main__':
   main()


