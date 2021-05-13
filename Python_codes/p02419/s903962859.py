import sys

#fin = open("test.txt", "r")
fin = sys.stdin

w = fin.readline()
w = w.rstrip('\n')
w = w.lower()

s = fin.read()
s = s.lower()
s = s.replace('\n', ' ')

s_list = s.split()
idx = 0
count = 0

for e in s_list:
	if w == e:
		count += 1

print(count)