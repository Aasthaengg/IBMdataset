def judge(A, B, C):
  if A < B:
    if B < C:
      return True
  return False
  
A, B, C = map(int, input().split())
K = int(input())
ans = "No"
for _ in range(K):
  if B <= A:
    B = B * 2
  elif C <= B:
    C = C * 2
  
  if judge(A, B, C):
    ans = "Yes"
    break
print(ans)
