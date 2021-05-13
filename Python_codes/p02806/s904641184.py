n = int(input())
ss = []
ts = []
for _ in range(n):
	s, t = input().split()
	ss.append(s)
	ts.append(int(t))
x = input()

idx = ss.index(x)
ans = 0
for i in range(idx+1, n):
	ans += ts[i]
print(ans)