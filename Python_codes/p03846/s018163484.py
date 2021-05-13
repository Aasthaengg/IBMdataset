from collections import Counter

N = int(input())
A = [0] + list(map(int, input().split()))
p = 10**9 + 7
l = Counter(A)

flag = True
for i in range(N%2 == 0,N,2):
  if l[i] != 2:
    flag = False
    break
if flag:
  print(pow(2,N//2,p))
else:
  print(0)