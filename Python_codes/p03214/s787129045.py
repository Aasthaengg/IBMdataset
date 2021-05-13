n = int(input())
A = list(map(int,input().split()))
ave = sum(A)/n
for i in range(n):
  A[i] = abs(A[i]-ave)
a = min(A)
for j in range(n):
  if A[j] == a:
    print(j)
    exit()