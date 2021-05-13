N = int(input())
M = {}
S = set()
for i in range(N):
	s, p = input().split()
	if s in M:
		t = M[s]
		t.append((int(p), i + 1))
	else:
		t = []
		t.append((int(p), i + 1))
		M[s] = t		
	S.add(s)

for s in sorted(S):
	for t2 in (sorted(M[s], reverse = True)):
		print(t2[1])
	
