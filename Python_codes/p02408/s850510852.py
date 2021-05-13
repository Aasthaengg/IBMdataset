N = int(input())

#??????????????????????????????
FL =[]
for i in range(13):
 FL.append("S " + str(i+1))
for i in range(13):
 FL.append("H " + str(i+1))
for i in range(13):
 FL.append("C " + str(i+1))
for i in range(13):
 FL.append("D " + str(i+1))

for i in range(N):
 D = str(input())
 FL.remove(D)

for i in range(52 - N):
 print(FL[i])