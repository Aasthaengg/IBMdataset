from bisect import *
N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))

count = 0

for i in range(N):
  a = bisect_left(A, B[i])
  c = bisect(C, B[i])
  c = N - c
  count += (a*c)

print(count)