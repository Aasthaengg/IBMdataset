numberOfDataSets = 0
sideLengthList = []

while 1:
	try:
		data = raw_input().split()

		if len(data) == 1 :
			numberOfDataSets = int(data[0])

			if numberOfDataSets != 0 :
				sideLengthList = []

		elif len(data) == 3 and numberOfDataSets != 0:
			numberOfDataSets -= 1
			sideLengthList.append(data)
 
		if numberOfDataSets == 0 :
			# Is it a right triangle?
			for i in range(0, len(sideLengthList)) :

				a = int(sideLengthList[i][0])*int(sideLengthList[i][0])
				b = int(sideLengthList[i][1])*int(sideLengthList[i][1])
				c = int(sideLengthList[i][2])*int(sideLengthList[i][2])

				if a + b == c or b + c == a or c + a == b :
					print"YES"
				else:
					print"NO"

	except:
		break