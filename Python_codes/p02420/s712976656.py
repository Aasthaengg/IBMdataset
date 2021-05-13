import sys
dataset = sys.stdin.readlines()

seq = 0

while dataset[seq] != '-\n':
 s = dataset[seq]
 l = len(s) - 1
 s = s[:l]
 seq += 1
 n = dataset[seq]
 l = len(n) - 1
 n = int(n[:l])
 seq += 1
 for i in range(seq, seq + n):
  h = dataset[i]
  l = len(h) - 1
  h = int(h[:l])
  s = s[h:] + s[0:h]
 print(s)
 seq += n