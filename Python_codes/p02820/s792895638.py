N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()
ans = 0

for i in range(K):
  last = "D"
  wl = "l"
  for j in range(N//K+1):
    if  j*K + i >= N:
      break
    else:
      te = T[j*K+i]
      if te != last:
        last = te
        wl = "w"
        if te == "r":
          ans += P
        elif te == "s":
          ans += R
        else:
          ans += S
      else:
        if wl == "l":
          last = te
          wl = "w"
          if te == "r":
            ans += P
          elif te == "s":
            ans += R
          else:
            ans += S
        else:
          last = te
          wl = "l"
print(ans)

