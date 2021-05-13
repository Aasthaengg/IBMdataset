n = int(input())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))
ans = 0
for i in range(n):
  if list_A[i] >= list_B[i]:
    list_A[i] -= list_B[i]
    ans += list_B[i]
    list_B[i] = 0
  else:
    ans += list_A[i]
    list_B[i] -= list_A[i]
    list_A[i] = 0
    if list_B[i] > list_A[i+1]:
      ans += list_A[i+1]
      list_A[i+1] = 0
    else:
      ans += list_B[i]
      list_A[i+1] -= list_B[i]
print(ans)