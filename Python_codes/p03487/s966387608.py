import numpy as np
def main():
  N = int(input())
  A = list(map(int, input().split()))
  dic = {}
  for i in range(N):
    if not A[i] in dic:
      dic[A[i]]=1
    else:
      dic[A[i]]+=1
  ans = 0
  for i, j in dic.items():
    if i < j:
      ans += j-i
    if j < i:
      ans += j
  print(ans)
  
if __name__ == "__main__":
  main()