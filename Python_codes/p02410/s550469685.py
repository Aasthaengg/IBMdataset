input = raw_input().split(" ")
n = int(input[0])
m = int(input[1])

i = 0
vec_a = []
while i < n:
  line = map(int, raw_input().split(" "))
  vec_a.append(line)
  i += 1
i = 0
vec_b = []
while i < m:
  line = int(raw_input())
  vec_b.append(line)
  i += 1
# print vec_a
# print vec_b

vec_c = []
for i in vec_a:
  sum = 0
  for j in xrange(m):
    sum += i[j] * vec_b[j]
  vec_c.append(sum)

for i in vec_c:
  print i