import sys

# A - Kenken Race
def can_goal(start, goal):
	global S

	way = S[start:goal+1]

	if not '##' in way:
		return True


def can_go_halfway(start, goal):
	global S

	way = S[start:goal+1]

	if way.find('...') > -1:
		return True


N, A, B, C, D = map(int, input().split())
S = input()
S = '.' + S

if C < D:
	if can_goal(B, D):
		if can_goal(A, C):
			print('Yes')
			exit()
else:
	if can_go_halfway(B - 1, D + 1):
		if can_goal(A, C):
			if can_goal(B, D):
				print('Yes')
				exit()

print('No')