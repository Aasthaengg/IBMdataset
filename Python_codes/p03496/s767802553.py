from numpy import argmax, argmin
N = int(input())
a = list(map(int,input().split()))

a_max = max(a)
a_argmax = argmax(a)
a_min = min(a)
a_argmin = argmin(a);

ans = ''
if abs(a_max) >= abs(a_min):
	ans += '{}\n'.format(2 * N - 1)
	for i in range(N):
		ans += '{} {}\n'.format(a_argmax + 1, i + 1)
	for i in range(1, N):
		ans += '{} {}\n'.format(i, i + 1)
else:
	ans += '{}\n'.format(2 * N - 1)
	for i in range(N):
		ans += '{} {}\n'.format(a_argmin + 1, i + 1)
	for i in range(N, 1, -1):
		ans += '{} {}\n'.format(i, i - 1)
ans=ans[:-1]

print(ans)