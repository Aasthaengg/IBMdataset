n = int(input())
s = [int(x) for x in input().split()]
q = int(input())
t = [int(x) for x in input().split()]

cnt = 0

for x in t:
	if x in s:
		cnt += 1

print(cnt)