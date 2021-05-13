n = int(input())
txy = [list(map(int, input().split())) for _ in range(n)]

T=X=Y=0
ok = True
for t,x,y in txy:
  if abs(X-x)+abs(Y-y) <= t-T:
    if (t-T)%2 == 0:
      if (abs(X-x)+abs(Y-y))%2!=0:
        ok = False
        break
    else:
      if (abs(X-x)+abs(Y-y))%2==0:
        ok = False
        break
  else:
    ok = False
    break
  T,X,Y = t,x,y
print("Yes" if ok else "No")