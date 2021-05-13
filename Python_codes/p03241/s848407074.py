N, M = map(int,input().split())

s = M//N
for i in reversed(range(1,s+1)):
  if M%i == 0:
    ans = i
    break
print(ans)