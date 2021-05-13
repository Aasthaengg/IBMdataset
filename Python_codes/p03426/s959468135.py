import sys
input = sys.stdin.readline

h, w, d = map(int, input().split())
n = h*w
place = [0]*n
for i in range(h):
  a = [int(x) for x in input().split()]
  for j in range(w):
    place[a[j]-1] = (i, j)

bit = [0]*n
for i in range(n):
  if i < d:
    continue
  bit[i] = bit[i-d]+abs(place[i][0]-place[i-d][0])+abs(place[i][1]-place[i-d][1])

q = int(input())
for i in range(q):
  l, r = map(int, input().split())
  print(bit[r-1]-bit[l-1])