N = int(input())
A = list(map(int, input().split()))
each = [0] * N

for i in range(N):
  if i + 1 == A[i]:
    each[i] = 1
    
#print(each)
ans = 0
for i in range(N):
  if i < N - 1:
    if each[i] == 1:
      if each[i + 1] == 1:
        ans += 1
        each[i + 1] = 0
      else:
        ans += 1
  else:
    if each[i] == 1:
      ans += 1
  #print(each, ans)      
print(ans)
