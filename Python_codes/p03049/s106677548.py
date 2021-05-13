import collections
c = 0
cc = collections.Counter()
for _ in range(int(raw_input())):
	w = raw_input()
	for u in range(len(w)-1):
		if w[u:u+2] == 'AB': c+=1
	w = w.replace('AB','')
	if len(w) == 1:
		s = (w[0] if w[0] == 'A' or w[0] == 'B' else '')
	if len(w) >= 2:
		s = (w[0] if w[0] == 'A' or w[0] == 'B' else '') + (w[-1] if w[-1] == 'A' or w[-1] == 'B' else '')
	
	if s: cc[s]+=1
q= 0 #max(0,cc['BA'] - 1)
if cc['BA']:
	q += cc['BA'] -1
	if cc['A']:
		cc['A']-=1
		q+=1 
	if cc['B']:
		cc['B']-=1
		q+=1 
print c + q + min(cc['A']+cc['AA'],cc['B']+cc['BB'])
"""
A
AA
B
BB
AB
BA

 A - [BA - BA - BA - BA - BA - BA]  - B 
 A - B 



    [AB - AB - AB - AB - AB - AB ]

    A - B - A  - B  

"""