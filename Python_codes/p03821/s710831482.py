import math
def myAnswer(N:int,A:list,B:list) -> int:
   ans = 0
   A.reverse()
   B.reverse()
   for a,b in zip(A,B):
      a += ans
      target =math.ceil(a/b) * b - a
      ans += target
   return ans

def modelAnswer():
   return
def main():
   N = int(input())
   A = []
   B = []
   for _ in range(N):
      a,b = map(int,input().split())
      A.append(a)
      B.append(b)
   print(myAnswer(N,A,B))
if __name__ == '__main__':
   main()