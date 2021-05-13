priceList = []
t = raw_input()


for i in range(int(t)):
    priceList.append(int(input()))

maxv = -2000000000
minv = priceList[0]

for i in range(1, int(t)):
	if maxv < priceList[i] - minv:
		maxv = priceList[i] - minv
	if minv > priceList[i]:
		minv = priceList[i]
    
print maxv