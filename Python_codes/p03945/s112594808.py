import itertools

S=input()

S_=itertools.groupby(S)
cnt=-1
for key,gr in S_:
	cnt+=1

print(cnt)