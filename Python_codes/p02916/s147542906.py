N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

score = sum(B)
num = A[0]
for i in A:
  if num == i-1:
    score += C[i-2]
  num = i
print(score)