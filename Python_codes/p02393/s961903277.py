s = raw_input()
nlist = map(int, s.split())
a, b, c= nlist
#print nlist.sort() 
ls = sorted(nlist)
print '%d %d %d' %(ls[0], ls[1], ls[2])