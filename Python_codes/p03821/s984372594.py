n = int(input())
A = [0]*n
B = [0]*n
for i in range(n):
  A[i],B[i] = map(int,input().split())

ans = 0
for i in range(n)[::-1]:
  j = i  
  tmp = (A[j]+ans) % B[j]
  if tmp:
    ans += B[j] - tmp
  
print(ans)  