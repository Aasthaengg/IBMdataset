n,k = [int(s) for s in input().split()]
#n,k = [int(s) for s in data.pop().split()]
#n,k = 100000,100000
w_org = []
[w_org.append(int(input())) for i in range(n)]
#[w_org.append(int(data.pop())) for i in range(n)]
#w_org = [1 for i in range(n)]


def can(p_org,k):
	p = p_org
	w = w_org[::-1]
	while k and w:
		ww = w[-1]
		if ww <= p:
			p -= ww
			w.pop()
		else:
			p = p_org
			k -= 1
		if p == 0:
			p = p_org
			k -= 1
		#print(ww,k,p)
	return not(w)


left,right = max(w_org)-1,sum(w_org)+1
roop = 0
while left+1 < right:
	roop += 1
	middle = (left+right) // 2
	if can(middle,k):
		right = middle
	else:
		left = middle
print(right)