N = int(input())
a = list(map(int, input().split()))

res = 0
for i in range(N):
  fi_flg = False
  while fi_flg is False:
    if a[i] % 2 == 0:
      a[i] = int(a[i]/2)
      res += 1
    else:
      fi_flg = True
      
print(res)