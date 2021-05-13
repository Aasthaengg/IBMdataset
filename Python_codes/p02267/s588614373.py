import sys

#fin = open("test.txt", "r")
fin = sys.stdin

n = int(fin.readline())
S = list(map(int, fin.readline().split()))
q = int(fin.readline())
T = list(map(int, fin.readline().split()))

ret = 0

for t in T:
	for s in S:
		if t == s:
			ret += 1
			break

print(ret)