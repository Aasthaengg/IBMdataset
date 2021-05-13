from collections import deque
N = int(input())
used1 = [0] * N
used2 = [0] * N

ans_list = [0] * 500
for i in range(1, 500):
  ans_list[i] = int(i * (i + 1) // 2)

if N in ans_list:
  print("Yes")
  k = ans_list.index(N)
  print(k + 1)
  A = [deque([]) for i in range(k)]
  for i in range(1, N + 1):#最大10 ** 5
    p = int(((1 + 8 * i) ** (1/ 2) - 1.001) // 2)
    A[p].append(i)
  #print(A)
  #print(A[1][0])
  for i in range(k):
    print(k, end = " ")
    for j in range(i + 1):
      #print("j", j)
      print(A[i][j], end = " ")
    for l in range(i + 1, k):
      print(A[l][i], end = " ")
    print("")
  
  print(k, end = " ")
  for i in range(k):
    print(A[i][i], end = " ")
  print("")
else:
  print("No")