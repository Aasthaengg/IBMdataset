N = int(input())
S = [0 if s == "#" else 1 for s in list(input())]
ruisekiwa = [0]*(N+2)
i = 1
r = 0
while i <= N:
  r = r+S[i-1]
  ruisekiwa[i] = r
  i += 1
ruisekiwa[N+1] = ruisekiwa[N]
ans = 10**10
i = 1
while i <= N+1:
  towhite = (i-1)-(ruisekiwa[i-1]-ruisekiwa[0])
  toblack = ruisekiwa[N+1]-ruisekiwa[i-1]
  ans = min(ans, towhite+toblack)
  i += 1
print(ans)