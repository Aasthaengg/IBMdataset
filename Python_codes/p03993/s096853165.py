n = int(input())
A = list(map(int, input().split()))

cnt = 0
for itr, val in enumerate(A):
  if A[val - 1] == itr + 1:
    cnt += 1
    
print(cnt // 2)