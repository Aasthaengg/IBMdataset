A1,A2,A3 = map(int, input().split())
res = 100*3
A = [A1,A2,A3]
arr = [[0,1,2], [0,2,1], [1,0,2], [1,2,0],[2,0,1], [2,1,0] ]
for a in arr:
  m = abs(A[  a[0] ] - A[a[1]])
  n = abs(  A[ a[2] ] - A[a[1]])
  if res > m + n:
    res = m + n
print(res)