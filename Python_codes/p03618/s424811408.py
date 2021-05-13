from collections import Counter
a = input()
c,ans = Counter(a),1+len(a)*(len(a)-1)//2
for i in c.most_common():
	if i[1]==1: break
	else: ans -= i[1]*(i[1]-1)//2
print(ans)