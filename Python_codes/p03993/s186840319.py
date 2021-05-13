N = int(input())
A = [int(i) for i in input().split()]
cnt = 0
for i, a in enumerate(A):
  if A[a-1]-1 == i:
    cnt += 1
  
print(cnt//2)