n = input()
s = len(n)-1

def calc(n,op):
  tmp = int(n[0])
  for i in range(len(op)):
    if op[i] == '+':
      tmp += int(n[i+1])
    else:
      tmp -= int(n[i+1])
  return tmp
for j in range(2**s):
  op = ''
  for k in range(s):
    if (j>>k)&1:
      op += '+'
    else:
      op += '-'
  if calc(n,op) == 7:
    ret = ''
    for l in range(len(op)):
      ret += n[l]
      ret += op[l]
    ret += n[-1]
    ret +='=7'
    print(ret)
    exit(0)