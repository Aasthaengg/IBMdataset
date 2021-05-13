mat = [map(int ,raw_input().split()) for _ in range(3)]
def f(m):
	return (m[1] - m[0], m[2] - m[1])
b = True
s =set([])
for l in mat:
	s.add(f(l))
if len(s) >1:
	b = False
s = set([])
for j in range(3):
	c = [mat[i][j] for i in range(3)]
	s.add(f(c))
if len(s) >1:
	b = False
print 'Yes' if b else 'No'