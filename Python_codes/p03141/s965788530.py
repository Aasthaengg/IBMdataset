N = int(input())
base = 0
L = []
for _ in range(N):
	ta,tb = map(int,input().split())
	base -= tb
	L.append(ta+tb)

L.sort(reverse = True)

takahashi = 0

for i in range(0,N,2):
	takahashi += L[i]

print(takahashi + base)