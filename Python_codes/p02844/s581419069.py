import sys
readline = sys.stdin.readline

N = int(readline())
S = readline().rstrip()

ans = 0
for i in range(1000):
  target = str(i).zfill(3)
  ind = 0
  tar_ind = 0
  while ind < N:
    if S[ind] == target[tar_ind]:
      tar_ind += 1
      if tar_ind == 3:
        ans += 1
        break
    ind += 1
  
print(ans)