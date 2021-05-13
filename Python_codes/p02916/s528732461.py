N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
ans = 0
bef = 100

for a in A:
  ans+=B[a-1]
  if a-bef == 1:
    ans+=C[a-2]
  bef = a
  
print(ans)