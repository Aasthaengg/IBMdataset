A = list(map(int, input().split()))
if A[0]%3 ==0 or A[1]%3 == 0 or (A[0] +A[1])%3 ==0:
  print('Possible')
  exit()
print('Impossible')