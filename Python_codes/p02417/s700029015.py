# -*- coding: utf-8 -*-
tset = [0] * 27
while 1:
 try:
  str = raw_input().lower()
  a = ord('a')
  for c in str:
   tset[ord(c)-a if c.islower() else 26] += 1
 except EOFError:
  for c in xrange(26):
   print "{0} : {1}".format(chr(a+c), tset[c])
  break