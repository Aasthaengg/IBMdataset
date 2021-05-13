# -*- coding: utf-8 -*-
while 1:
 s = raw_input()
 if s=="-": break
 n = input()
 t = sum([input() for i in xrange(n)]) % len(s)
 print s[t:] + s[:t]