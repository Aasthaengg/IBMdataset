n = int(input())
sa = []
for i in range(n):
  a,b = list(map(int, input().split()))
  if ( a > b ):
    print('No')
    exit()    
  sa.append({'a': a, 'b': b})

sa.sort(key=lambda x: x['b'])

aa = 0
for i in range(n):
  aa = aa + sa[i]['a']
  if (aa > sa[i]['b']):
    print('No')
    exit()

print('Yes')

