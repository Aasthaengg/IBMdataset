n = int(input())
S = input()
L = []
ans = 0
for i in range(10):
  for j in range(10):
    for k in range(10):
      cnt = 0
      iflag = 0
      jflag = 0
      while True:
        if cnt >= n:
          break
        if iflag == 0 and S[cnt] == str(i):
          iflag = 1
          cnt += 1
          continue
        if iflag == 1 and jflag == 0 and S[cnt] == str(j):
          jflag= 1
          cnt += 1
          continue
        if jflag == 1 and S[cnt] == str(k):
          ans += 1
          break
        cnt += 1

print(ans)