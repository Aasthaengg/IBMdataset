n = int(input())
A = input().split()
A.append("#")
ans = 0
c = 0
for i in range(n):
  c += 1
  if A[i] != A[i+1]:
    ans += c//2
    c = 0
print(ans)