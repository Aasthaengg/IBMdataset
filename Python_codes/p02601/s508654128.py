A,B,C = map(int,input().split())
K = int(input())
for k in range(K):
  if B <= A:
    B *= 2
    continue
  if C <= B:
    C *= 2
    continue
if B > A and C > B:
  print('Yes')
else:
  print('No')