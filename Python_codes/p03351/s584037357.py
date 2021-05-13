A, B, C, D = map(int, input().split())
ans="No"
if abs(C-A)<=D or abs(B-A)<=D and abs(C-B)<=D:
  ans = 'Yes'
print(ans)