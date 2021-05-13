import math
def myAnswer(K:int,A:int,B:int) -> int:
   if(K <= A-1): return K+1
   tmp =(K - (A-1))
   # print(tmp)
   ans = (B - A) * math.floor(tmp//2) + tmp % 2 + A
   # print(ans)
   return max(ans,K+1)



def modelAnswer():
   return
def main():
   K,A,B = map(int,input().split())
   print(myAnswer(K,A,B))
if __name__ == '__main__':
   main()