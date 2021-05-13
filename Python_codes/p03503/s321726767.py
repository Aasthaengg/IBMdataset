import numpy as np
n = 10
bit_base = 2#bit_base^nの全探査になる. 
def Base_10_to_n(X, n):#10進数をbit_base進数に変換
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out
  
def main():
  N = int(input())
  F = []
  for i in range(N):
    F.append(list(map(int, input().split())))
  F = np.array(F)
  P = []
  for i in range(N):
    P.append(list(map(int, input().split())))
  ans = -1*10**9
  for i in range(bit_base**n):
    if i == 0: continue
    s = Base_10_to_n(i, bit_base)
    s = s.zfill(n)
    for num, j in enumerate(s):
      ans_temp = 0
      s = list(s)
      s = np.array([int(i) for i in s])
      C = np.sum(F*s, axis = 1)
      for k,c in enumerate(C):
        ans_temp += (P[k][c])
      ans = max(ans, ans_temp)
  print(ans)
if __name__ == "__main__":
  main()