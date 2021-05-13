from collections import Counter as C
input()
D=C(list(map(int,input().split())))
input()
T=C(list(map(int,input().split())))
for t in T:
  if T[t]>D[t]:
    print('NO')
    exit()
print('YES')