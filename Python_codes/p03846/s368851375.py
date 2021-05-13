N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
n = N-1
for i in range(N//2):
  if A[2*i]!=n or A[2*i+1]!=n:
    print(0)
    exit()
  n -= 2
  
if N&1 and A[-1]!=0:
  print(0)
  exit()

print((1<<N//2)%(10**9+7))
