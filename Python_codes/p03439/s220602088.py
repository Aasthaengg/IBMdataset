N = int(input())

print(0)
s = input()
if s == 'Vacant':
  quit()

root = 0
num = N - 1 # root以外の席数 (<- 偶数)
while True:
  n = num // 2
  print((root + n)%N)
  _s = input()
  if _s == 'Vacant':
    quit()
  if (s==_s and n%2==0) or (s!=_s and n%2==1):
    root += n
    s = _s
    num = n + (n%2==1)
  else:
    num = n - 1 + (n%2==0)