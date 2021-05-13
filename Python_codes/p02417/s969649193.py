from string import ascii_lowercase as asc
import sys
sen = sys.stdin.read()
sent = list(sen.lower())
for i in asc:
	print(i,":",sent.count(i))
