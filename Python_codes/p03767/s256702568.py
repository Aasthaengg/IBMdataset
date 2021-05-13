
def myAnswer(N:int,A:list) -> int:
   ans = 0
   A.sort(reverse= True)
   for i in range(1,N*2,2):
      ans += A[i]
   return ans


def modelAnswer():
   tmp=1
def main():
   N = int(input())
   A = list(map(int,input().split()))
   print(myAnswer(N,A[:]))
if __name__ == '__main__':
   main()