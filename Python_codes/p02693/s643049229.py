K = int(input())
A,B = (int(x) for x in input().split())

for i in range(B-A+1):
  if (A+i) % K == 0:
    print('OK')
    break
  elif i == B-A:
    print('NG')