s = input()
K = int(input())
N = len(s)
l = []
cnt = 0
for i in range(N):
	for j in range(i+1, min(i+K+1, N+1)):
		l.append(s[i:j])

l = list(set(l))
l.sort()
print(l[K-1])