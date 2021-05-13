# (c) midandfeed
q = [int(x) for x in input().split()]
ans = True
for i in range(1, len(q)):
	ans = ans and (q[i-1] < q[i])
	
print("Yes" if ans else "No")