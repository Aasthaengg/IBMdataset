# _*_ coding:utf-8 _*_
#  CADDi2018 for Beginners A 1222
#  https://atcoder.jp/contests/caddi2018b/tasks/caddi2018b_a

def  counter2(forSizeInteger):
	forSizeString = str(forSizeInteger)
	counter = 0
	if(forSizeString[0]=='2'):
		counter = counter + 1
	if (forSizeString[1] == '2'):
		counter = counter + 1
	if (forSizeString[2] == '2'):
		counter = counter + 1
	if (forSizeString[3] == '2'):
		counter = counter + 1

	answer=counter

	return answer


if __name__ == '__main__':
	n = int(input())
	solution=counter2(n)
	print(solution)