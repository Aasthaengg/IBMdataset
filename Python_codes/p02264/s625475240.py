import sys
data = []
for line in sys.stdin:
	data.append(line.split())

quontum = int(data[0][1])
targetData = data[1:]
answerData = []
totalQuontum = 0

while targetData :
	target = targetData.pop(0)

	target[1] =  int(target[1]) - quontum

	if target[1]<= 0:
		totalQuontum += quontum + int(target[1])
		target[1] = totalQuontum
		answerData.append(target)
	else :
		targetData.append(target)
		totalQuontum += quontum

for answer in answerData:
	print(str(answer[0]) + ' ' + str(answer[1]))
