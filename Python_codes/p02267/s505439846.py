def find(target, list):
  for i in xrange(len(list)):
    if target == list[i]:
      return 1
  return 0


n = int(raw_input())
S = raw_input().split()
q = int(raw_input())
T = raw_input().split()
count = 0
for i in xrange(q):
  count += find(T[i], S)
print count