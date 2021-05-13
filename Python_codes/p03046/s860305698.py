m,k = map(int,input().split())

if k>=2**m:
  print(-1)

elif m == 0:
  print(" ".join(["0","0"]))

elif m == 1 and k == 0:
  print("0 0 1 1")

elif m == 1 and k == 1:
  print(-1)

elif m >= 2:
  b = [i for i in range(2**m)]
  b.remove(k)
  c = sorted(b,reverse = True)
  ans = b + [k] + c + [k]
  ans = list(map(str,ans))
  print(" ".join(ans))