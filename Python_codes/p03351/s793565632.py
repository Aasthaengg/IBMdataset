A, B, C, D = map(int, input().split())
ans = 'Yes'
AB = abs(A-B)
AC = abs(A-C)
BC = abs(B-C)

if AC > D:
  if AB > D or BC > D:
    ans = "No"
print(ans)