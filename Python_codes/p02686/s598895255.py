def pdebut(s):
	o = 0
	for c in s:
		if c=='(':o+=1
		else: o-=1
		if o<0 : return False
	return o>=0
	
def pfin(s):
	c = 0
	for o in s[::-1]:
		if o==')':
			c+=1
		else:c-=1
		if c<0: return False
	return c>=0
	
def valuer(s):
	o = 0
	for c in s:
		if c=='(':o+=1
		else: o-=1
	return o
	
n = int(input())
val = [0]*(n+1)
tab = []
debut = []
fin = []
milieu = []
for i in range(n):
	s = input()
	tab.append(s)
	if pdebut(s):
		debut+=[i]
	elif pfin(s):
		fin+=[i]
	else:
		val[i] = valuer(s)
		milieu+=[i]

def cle(x):
	return -x[1]		
couples = [[i,val[i]] for i in milieu]
couples.sort(key = cle)

S = "".join(tab[i] for i in debut)
S+="".join(tab[c[0]] for c in couples)
S+= "".join(tab[i] for i in fin)

# ~ print("debut",debut)
# ~ print("milieu",milieu)
# ~ print("fin",fin)

# ~ print(S)

def Bon(s):
	o = 0
	for c in s:
		if c=='(':o+=1
		else: o-=1
		if o<0 : return False
	return o==0
print("Yes" if Bon(S) else "No")
