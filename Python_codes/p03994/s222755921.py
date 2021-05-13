S = list(input())
K = int(input())

for i in range(len(S)):
  n = ord(S[i])
  if S[i] == 'a':
    continue
  if ord('z') - n + 1 <= K:
    K -= ord('z') - n + 1
    S[i] = 'a'
assert K >= 0
if K != 0:
  n = ord(S[-1])
  n -= ord('a')
  n += K
  n %= 26
  n += ord('a')
  S[-1] = chr(n)
print(''.join(S))
    
    
