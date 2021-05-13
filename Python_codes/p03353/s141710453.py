#X = ["a", "ba", "zxx", "abb", "ab"]
#print(sorted(X))

s = str(input())
K = int(input())
ans = []
N = len(s)

for i in range(N):
  y = min(N + 1, i + K + 1)
  for j in range(i + 1,y):
    x = s[i:j]
    if x not in ans:
      ans.append(x)
#print(ans)
  
print(sorted(ans)[K - 1])
