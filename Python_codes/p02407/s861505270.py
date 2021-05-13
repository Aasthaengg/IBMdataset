n = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

strA = ''
for ra in reversed(a):
  strA += '{0} '.format(ra)
print(strA[:-1])