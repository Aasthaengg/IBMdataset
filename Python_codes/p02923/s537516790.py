a = int(input())
b = list(map(int,input().split()))
c = 0
ans = 0
for i in range(a-1):
  if b[i] >= b[i+1]:
    c += 1
  else:
    ans = max(ans,c)
    c = 0
print(max(c,ans))