n = raw_input()
S = map(int, raw_input().split())
q = raw_input()
T = map(int, raw_input().split())

cnt = 0
for i in T:
	if i in S:
		cnt += 1

print cnt