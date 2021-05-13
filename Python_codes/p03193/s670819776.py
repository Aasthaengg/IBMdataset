# _*_ coding:utf-8 _*_
#  CADDi2018 for Beginners B AtCoderAlloy
#  https://atcoder.jp/contests/caddi2018b/tasks/caddi2018b_b

def checkGetArroy(getArroyHeight,getArroyWidth,nowArroyHeight,nowArroyWidth):
	if(getArroyHeight <= nowArroyHeight) and (getArroyWidth <= nowArroyWidth):
		return True
	else:
		return False


def countGetArroy(allArroyNumber,arroyHeight,arroyWidth,eachArroyHeightList,eachArroyWidthList):

	counter = 0
	patternRange = range(0,allArroyNumber,1)
	for i in patternRange:
		checkResult = checkGetArroy(arroyHeight,arroyWidth,eachArroyHeightList[i],eachArroyWidthList[i])
		if (checkResult==True):
			counter = counter + 1

	return counter


if __name__ == '__main__':
	n , h , w = map(int,input().strip().split(' '))
	alloyRange = range(0,n,1)
	heightList = []
	widthList = []
	for i in alloyRange:
		tmpHeight,tmpWidth = map(int,input().strip().split(' '))
		heightList.append(tmpHeight)
		widthList.append(tmpWidth)
	solution=countGetArroy(n,h,w,heightList,widthList)
	print(solution)