from collections import Counter
N = int(input())
A = list(map(int,input().split()))
C = Counter(A)

cnt = 0
for i in set(A):
  I = C[i]
  if I == i:
    continue
  elif I > i:
    cnt += I - i
  else :
    cnt += I
  
print(cnt)