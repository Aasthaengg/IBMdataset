import sys

def encode(n:int) -> str:
  if n == 0:
      return '0'

  if n == 1:
      return '1'

  if n % 2 == 1:
      ans = '{}1'.format(encode((n-1) // (-2)))
      sys.stderr.write('{} for {}'.format(ans, n))
      sys.stderr.write('\n')
      return ans

  if n % 2 == 0:
      ans = '{}0'.format(encode(n // (-2)))
      sys.stderr.write('{} for {}'.format(ans, n))
      sys.stderr.write('\n')

      return ans

n = int(input())
ans = encode(n)
print(ans)

  
