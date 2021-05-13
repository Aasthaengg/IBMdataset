N = int(input())
A = list(map(int, input().split()))
 
ans = float("inf")
for i in range(N):
  a = A[i]
  ans_tmp = 0
  while a%2==0:
    a = a//2
    ans_tmp += 1
  ans = min(ans_tmp, ans)
print(ans)