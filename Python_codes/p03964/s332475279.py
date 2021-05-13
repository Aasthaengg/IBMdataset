import math

N = int(input())
t,a = [],[]
for _ in range(N):
	t_tmp, a_tmp = map(int, input().split())
	t.append(t_tmp)
	a.append(a_tmp)

T,A=1,1

for i in range(N):
	n = max(-(-A//a[i]), -(-T//t[i]))
	A = a[i] * n
	T = t[i] * n

print(A+T)