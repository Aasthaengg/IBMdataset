def main():
  import numpy as np
  N = int(input())
  A = list(map(int,input().split()))

  def ternary (n):
      if n == 0:
          return '0'
      nums = []
      while n:
          n, r = divmod(n, 3)
          nums.append(str(r))
      return ''.join(reversed(nums))

  ans = 0
  AA = np.array(A)
  for i in range(3**N):
    I = ternary(i).zfill(N)
    tmp = 1
    for a in range(N):
      if I[a] == "0":
        tmp *= AA[a] - 1
      elif I[a] == "1":
        tmp *= AA[a]
      else:
        tmp *= AA[a] + 1
    if tmp % 2 == 0:
      ans += 1
  print(ans)
main()  