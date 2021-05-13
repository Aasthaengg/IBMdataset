N = int(input())
D = list(map(int,input().split()))
D.sort()
M = int(input())
T = list(map(int,input().split()))
T.sort()

dindex = 0
for i in range(M):
  while 1:
    dindex += 1
    if T[i] == D[dindex-1]:
      break
    elif dindex == N:
      print('NO')
      exit()
print('YES')