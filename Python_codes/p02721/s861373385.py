n,k,c = map(int,input().split())
s = input()

forward = dict()
backward = dict()

rep = list(range(n))
# forward
l = 0
kf = k
kb = k
while 1:
  if s[l] == 'x':
    l += 1
  else:
    forward[k-kf] = l+1
    kf -= 1
    l += c+1
  if (l > n-1) | (kf == 0):
    break
rep.reverse()
# backward
l = n-1
while 1:
  if s[l] == 'x':
    l -= 1
  else:
    backward[kb-1] = l+1
    kb -= 1
    l -= c+1
  if (l < 0) | (kb == 0):
    break
#judgement
ret = set(forward.items()) & set(backward.items())
lis = list()
for l in range(len(ret)):
  lis.append(ret.pop()[1])
lis = sorted(lis)
lis.reverse()
for l in range(len(lis)):
  print(lis.pop())