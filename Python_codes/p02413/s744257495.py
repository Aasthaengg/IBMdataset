r,c = map(int,input().split())
data = [[0] * (c+1) for i in range(r)]
for row in range(r):
    data[row] = [int(i) for i in input().split()]
    data[row].append(sum(data[row]))
for row in range(r):
    for column in range(c+1):
        if column == (c):
            print(data[row][column])
        else: 
            print("%d " %data[row][column],end = "")
#転置

data_t = []
sumColumn = []
sumSumRow = 0
for column in range(c):
    dataRow = []
    for rowVector in data:
        dataRow.append(rowVector[column])
    data_t.append(dataRow) 

for column in data_t:
    sumColumn.append(sum(column))
for index in range(c):
    print("%d " %sumColumn[index],end = "")
for row in range(r):
    sumSumRow = sumSumRow + sum(data[row][:-1])
print("%d" % sumSumRow)

