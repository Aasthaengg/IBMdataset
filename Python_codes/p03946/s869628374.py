N, T = map(int,input().split())
A = list(map(int,input().split()))
max_profit = [0]
Min = A[0]
for i in range(N-1):
  if A[i] < Min:
    Min = A[i]
  if A[i+1] - Min > max_profit[0]:
    max_profit = [A[i+1] - Min]
  elif A[i+1] - Min == max_profit[0]:
    max_profit.append(A[i+1] - Min)
print(len(max_profit))

