N = int(input())
C = list(input())

W = C.count("W")
R = C.count("R")
w = 0
r = R

ans = R
for i in range(1,N+1):
  if C[i-1] == "W":
    w += 1
  else:
    r -= 1
  ans = min(ans, max(w,r))
  
print(ans)