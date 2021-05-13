n = int(input())
X = [list(input().split()) for i in range(n)]

ans = 0
for i in range(len(X)):
  if X[i][1] == "JPY":
    ans += float(X[i][0])
  else:
    ans += 380000.0 * float(X[i][0])
    
print(ans)