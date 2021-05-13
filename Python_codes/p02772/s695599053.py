import sys
N = int(input())
A = list(map(int,input().split()))
count = 0
frag = 0
for i in range(N):
  if A[i]%2 == 0:
    count = count+1
    if A[i]%3 == 0 or A[i]%5 == 0:
      frag = frag+1
if frag == count:
  print('APPROVED')
else:
  print('DENIED')