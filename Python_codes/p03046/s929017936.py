M, K = map(int, input().strip().split(' '))

MAX = 2 ** M

if K == 0:
  s = ' '.join(['{0} {0}'.format(i) for i in range(MAX)])
elif M == 1:
  s = '-1'
elif K < MAX:
  tmp = [i for i in range(MAX) if i != K]
  a = ' '.join(map(str, tmp))
  b = ' '.join(map(str, reversed(tmp)))
  s = '{0} {1} {0} {2}'.format(K, a, b)
else:
  s = '-1'

print(s)