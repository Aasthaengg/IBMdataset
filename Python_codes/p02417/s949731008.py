import sys

cc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
c  = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:
  s = sys.stdin.readline().rstrip('\r\n')
  if s == '':
    break

  for ii in range(len(s)):
    test = s[ii].lower()
    for jj in range(len(cc)):
      if test == cc[jj]:
        c[jj] += 1

for ii in range(len(cc)):
  print(cc[ii] +  ' : ' + str(c[ii]))

