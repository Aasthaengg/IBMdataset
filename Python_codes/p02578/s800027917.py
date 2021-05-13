N = int(input())
A = list(map(int, input().split()))
count = 0
max = A[0]
for i in range (0,N):
    while(max>A[i]):
        count = count + (max - A[i])
        A[i] = max
       # print(A)
    if(max<=A[i]):
        max = A[i]
      #  print(A)
print(count)