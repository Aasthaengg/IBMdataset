n,m = map(int,input().split())
ans = [0]*n
for i in range(m):
  s,c = map(int,input().split())
  if ans[s-1] != 0 and ans[s-1] != c:
    print(-1)
    exit()
  elif n != 1 and s == 1 and c == 0:
    print(-1)
    exit()
  else:
    ans[s-1] = c
ans_f = "".join((map(str,ans)))
if n>1 and ans_f[0] == "0":
  print("1"+ans_f[1::])
else:
  print(ans_f)
