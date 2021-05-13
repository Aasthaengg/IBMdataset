import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

"""
A<Bとする。
C<Dの場合：
A～CとB~Dの間に"##"が無ければ達成できる.
C>Dの場合：
上記に加え、B~Cの間に"..."が存在すれば達成できる
"""

n,a,b,c,d = map(int,readline().split())
s = readline().rstrip().decode('utf-8')
a,b,c,d = a-1,b-1,c-1,d-1

flag = 1
space = 0
res = 0
rock = 0
for i in range(a,c+1):
	if s[i] == "#":
		rock += 1
	else:
		rock = 0
	if rock >= 2:
		flag = 0
for i in range(b,d+1):
	if s[i] == "#":
		rock += 1
	else:
		rock = 0
	if rock >= 2:
		flag = 0
if c > d:
	for i in range(b-1,d+2):
		if s[i] == ".":
			space += 1
		else:
			res = max(res,space)
			space = 0
	res = max(res,space)
	if res < 3:
		flag = 0

print("Yes" if flag else "No")
