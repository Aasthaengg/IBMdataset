s = input()
st1=[]
st2=[]
st3=[]
n=len(s)
lv = 0
total=0
for i in range(n):
	c=s[i]
	if c=='\\':
		lv-=1
		st1.append(i)
	elif c=='/':
		lv+=1
		if len(st1) > 0:
			a = i - st1.pop()
			total+=a
			tmp=0	
			while len(st2)>0 and st2[-1]<lv:
				st2.pop()
				tmp+=st3.pop()
			st3.append(a+tmp)		
			st2.append(lv)
		elif len(st2) > 0:
			st2.pop()
			st2.append(lv)
		
print(total)
n = len(st3)
print(n,end='')
for i in range(n):
	print(' '+str(st3[i]),end='')
print()

