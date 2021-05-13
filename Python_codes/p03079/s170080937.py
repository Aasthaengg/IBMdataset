# _*_ coding:utf-8 _*_
#  Atcoder_Exawizards2019_Contest-A
#  TODO https://exawizards2019.contest.atcoder.jp/tasks/exawizards2019_a

def solveProblem(A,B,C):
	AminusB = A - B
	AminusC = A - C
	BminusC = B - C
	if AminusB == 0 and AminusC == 0 and BminusC == 0:
		answer = "Yes"
	else:
		answer = "No"
	return answer


if __name__ == '__main__':
	A,B,C = map(int,input().strip().split(' '))
	solution = solveProblem(A,B,C)
	print("{}".format(solution))
