def solve(i,m):
	if m == 0:
		return True
	if i >= n:
		return False
	res = solve(i+1,m) or solve(i+1,m-A[i])
	return res

n = int(input())
A = input()
A = [int(s) for s in A.split()]
q = int(input())
m = input()
m = [int(s) for s in m.split()]

ans = []
s = sum(A)
for mm in m:
	if s < mm:
		ans.append('no')
	else:
		ans.append({True:'yes',False:'no'}[solve(0,mm)])
#ans = [{True:'yes',False:'no'}[solve(0,mm)] for mm in m]
print('\n'.join(ans))