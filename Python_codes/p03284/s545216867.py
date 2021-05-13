nk = input()
nk_lis = nk.split()
n = int(nk_lis[0])
k = int(nk_lis[1])

if n % k == 0 :
  print(0)
elif n % k > 0:
  print(1)