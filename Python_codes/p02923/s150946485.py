N = int(input())
H = list(map(int, input().split()))
ans = 0
temp = 0
for i in range(N-1):
  if H[i] >= H[i+1]:
    temp += 1
  else:
    if temp > ans:
      ans = temp
    temp = 0
if temp > ans:
  ans = temp
  
print(ans)