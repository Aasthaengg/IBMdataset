A = list(map(int, input().split()))

answer = int(0)

for i in range(A[0],A[1]+1):
  if i % A[2] == 0:
    answer += 1
    
print(answer)