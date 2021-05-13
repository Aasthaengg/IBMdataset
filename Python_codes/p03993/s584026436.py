N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)
ans = 0
for i in range(1,N+1):
  if A[A[i]] == i:
    ans += 1
print(int(ans/2)) 