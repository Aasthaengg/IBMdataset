a= input()
b= input()
c= input()
qa=[]
qb=[]
qc=[]
for i in a:
	qa.append(i)
for i in b:
	qb.append(i)
for i in c:
	qc.append(i)
qa.append('d')
qb.append('d')
qc.append('d')
t=qa.pop(0)
while len(qa)>0 and len(qb)>0 and len(qc)>0:
	if t=='a':
		t=qa.pop(0)
	elif t=='b':
		t=qb.pop(0)
	else :
		t=qc.pop(0)

if len(qa)==0:
	print('A')
elif len(qb)==0:
	print('B')
else:
	print('C')