import sys
input =sys.stdin.readline

N=int(input().rstrip('\n'))
s = {}
for _ in range(N):
  A,B = (int(x) for x in input().rstrip('\n').split())
  if B in s:
    s[B] += A
  else:
    s[B] = A
m = sorted(list(set(s)))
check = 0
used = 0
for i in m:
  used += s[i]
  if used > i:
    check += 1
    print('No')
    break
if check == 0:
  print('Yes')
