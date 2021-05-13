def myAnswer(R:int,G:int,B:int,N:int) -> int:
   ans = 0
   for i in range(0,N+1,R):
      for j in range(0,N+1,G):
         k = N - j - i
         if( k % B != 0 or k < 0):
            continue
         else:
            # print(i,j,k)
            ans += 1

   return ans

def modelAnswer():
   return
def main():
   R,G,B,N = map(int,input().split())
   print(myAnswer(R,G,B,N))
if __name__ == '__main__':
   main()