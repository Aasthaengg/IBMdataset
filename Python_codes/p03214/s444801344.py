N = int(input())
A = list(map(int,input().split()))
ave = sum(A)/N
B = [0]*N
for i in range(N):
  B[i] = abs(A[i]-ave)
m = min(B)
for i in range(N):
  if B[i] == m:
    print(i)
    exit()