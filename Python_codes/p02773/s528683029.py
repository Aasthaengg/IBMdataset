N=int(input())
Sdict={}

for i in range(N):
	s=input()
	if s in Sdict:
		Sdict[s]+=1
	else:
		Sdict[s]=1

vmax=max(Sdict.values())

#Sdict_sorted=sorted(Sdict.items(), key=lambda x:x[1])
#print(Sdict_sorted)

anskeys = [k for k, v in Sdict.items() if v == vmax]
for ans in sorted(anskeys):
	print(ans)