Inp1 = list(input().split())
Inp1.extend(input().replace(' ',''))
Inp1.extend(input().replace(' ',''))

Inp_dict = {'1':0,'2':0,'3':0,'4':0}
for i in Inp1:
	Inp_dict[i] +=1

ans = list()
for k in Inp_dict.keys():
	if Inp_dict[k] == 2 : ans.extend(k)

if len(ans) == 2: print('YES')
else: print('NO') 