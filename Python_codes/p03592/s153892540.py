'''
Accepted    　:No
difficult   　:
ペナルティ　  　:5分
実際の回答時間  :分
WAの回数　     :回
合計時間　　  　:分
'''


def myAnswer(N: int, M: int, K: int) -> int:
   ans = set([0])
   for i in range(M):
      ans.add(N * (i + 1))
      ans.add(M - (i + 1) + (N - 1) * (i + 1))
   for i in range(N):
      ans.add(M * (i + 1))
      ans.add(N - (i + 1) + (M - 1) * (i + 1))
   print(ans)
   return "Yes" if K in ans else "No"

def modelAnswer(N,M,K):
   for k in range(N + 1):
      for l in range(M + 1):
         if k * (M - l) + l * (N - k) == K:
            return "Yes"
   return "No"
def main():
   N, M, K=map(int, input().split())
   print(modelAnswer(N, M, K))
if __name__ == '__main__':
   main()
