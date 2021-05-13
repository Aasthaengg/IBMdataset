N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = []

for n in range(N):
  ans+=[sum(A[:n+1])+sum(B[n:])]

print(max(ans))