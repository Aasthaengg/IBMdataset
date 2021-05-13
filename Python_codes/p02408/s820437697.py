#coding: UTF-8

x = int(input())
a = 0
s = 0
h = 0
c = 0
d = 0
lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
listh = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
listc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
listd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

while a < x:
	l = raw_input().split()
	a += 1
	m = l[0]
	n = int(l[1])
	
	if m == "S":
		s += 1
		lists.remove(n)
	if m == "H":
		h += 1
		listh.remove(n)
	if m == "C":
		c += 1
		listc.remove(n)
	if m == "D":
		d += 1
		listd.remove(n)

for ss in lists:
	print "S %d"%ss
for hh in listh:
	print "H %d"%hh
for cc in listc:
	print "C %d"%cc
for dd in listd:
	print "D %d"%dd