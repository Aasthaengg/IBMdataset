lst = input().split()
N = int(lst[0])
M = int(lst[1])

A = []
B = []

for i in range(N):
   A.append(input())

for i in range(M):
   B.append(input())

if A == B:
   print('Yes')
   exit()

for x in range(N-M):
   for y in range(N-M):
      count = 1
      for i in range(M):
         if A[y+i][x:x+M] != B[i]:
            count = 0
      if count == 1:
         print('Yes')
         exit()

print('No')