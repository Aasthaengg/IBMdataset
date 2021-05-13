N = int(input())
X = list(map (int, input().split()))
av = round(sum(X)/len(X))
ans = 0

for x in X:
  ans = ans + (av-x)**2
  
print(ans)