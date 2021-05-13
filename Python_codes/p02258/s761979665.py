n = input()
m = [0] * n
max_rieki = -1000000000



for i in xrange(n):
 m[i] = input()

min_rieki = m[0]
for i in xrange(1,n): 
  if max_rieki < m[i] - min_rieki:
     max_rieki = m[i] - min_rieki
  if min_rieki > m[i]:
     min_rieki = m[i]

print max_rieki