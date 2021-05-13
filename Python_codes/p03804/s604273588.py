n, m = map(int, input().split())
A = [input() for _ in range(n)]
B = [input() for _  in range(m)]

for i in range(n-m+1):
  if B[i] in A[i]:
    for j in range(m-1):
      if B[i+j] not in B[i+j]:
        print("No")
        exit()
    print("Yes")
    exit()
  else:
    print("No")
    exit()