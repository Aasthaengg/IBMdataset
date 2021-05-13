import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())

answer = "EQUAL"

if A > B:
	answer = "GREATER"
elif A < B:
	answer = "LESS"

print(answer)
