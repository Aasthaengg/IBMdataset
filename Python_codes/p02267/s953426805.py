# import sys

n = int(raw_input())
S = map(int, raw_input().strip(" ").split(" "))
q = int(raw_input())
T = map(int, raw_input().strip(" ").split(" "))

count = 0
for j in T:
	for n in S:
		if n == j:
			count += 1
			break

print count 