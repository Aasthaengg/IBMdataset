n = int(input())
A = list(map(int,input().split()))

ans = []
for i in range(n)[::-1]:
  for j in range(i+1)[::-1]:
    if j+1 == A[j]:
      ans.append(A.pop(j))
      break
      
if len(ans)==n:
  for a in ans[::-1]:
    print(a)
else:
  print(-1)