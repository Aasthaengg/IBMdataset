N = int(input())
A = sorted(map(int, input().split()))[::-1]
for i in range(N-3):
  if A[i]==A[i+1]==A[i+2]==A[i+3]:
    print(A[i]**2)
    exit()
  elif A[i]==A[i+1]:
    for j in range(i+2, N):
      if A[j]==A[j+1]:
        print(A[i]*A[j])
        exit()
    else:
      print(0)
      exit()
else:
  print(0)