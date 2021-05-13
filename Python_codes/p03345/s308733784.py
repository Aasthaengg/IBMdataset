def myAnswer(A:int,B:int,C:int,K:int) ->int :
   return B-A if(K %2 == 1) else -1*(B-A)
def modelAnswer():
   tmp=1
def main():
   A,B,C,K = map(int,input().split())
   ans = myAnswer(A,B,C,K)
   if(abs(ans) >= 10**18):
      print("Unfair")
   else:
      print(ans)

if __name__ == '__main__':
   main()