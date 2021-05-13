
def myAnswer(N:int)->int:
   K = len(str(N)) #桁数
   if(K == 1):return N
   c = N // 10**(K-1) #最上位の桁の数
   if((c*10**(K-1) + int("9"*(K-1)))<= N):
      return c + 9 *(K - 1)
   else:
      return c + 9 *(K - 1) -1 


def modelAnswer():
   tmp=1
def main():
   N = int(input())
   print(myAnswer(N))

if __name__ == '__main__':
   main()