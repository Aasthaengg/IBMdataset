N = int(input())
List_A = list(map(int, input().split()))
List_B = list(map(int, input().split()))
res = 0
for i in range(N):
  if List_A[i] >= List_B[i]:
    res += List_B[i]
  else:
    res += List_A[i]
    if List_A[i+1] >= List_B[i]-List_A[i]:
      res += List_B[i]-List_A[i]
      List_A[i+1] = List_A[i+1] - List_B[i] +List_A[i]
    else:
      res += List_A[i+1]
      List_A[i+1] = 0
print(res)