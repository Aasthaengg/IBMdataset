import math
N = int(input())
A = list(map(int,input().split()))
l = list()
ll = list()
for i in range(len(A)):
  if A[i]%4 == 0:
    l.append(A[i])
  if A[i]%2 == 0:
    ll.append(A[i])
four = len(l)
two = len(ll)-four
zero = N-two
a = math.floor(N/2)
if a <= four:
  print("Yes")
elif 2*a-two <= 2*four:
  print("Yes")
else:
  print("No")