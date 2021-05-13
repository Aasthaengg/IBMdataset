# Spreadsheet

sheet = [int(i) for i in input().rstrip().split()]
rows = sheet[0]
columns = sheet[1]

spreadSheet = []
for i in range(rows):
    row = [int(j) for j in input().rstrip().split()]
    rowTotal = 0
    for element in row:
        rowTotal += element
    row.append(rowTotal)
    spreadSheet.append(row)
# print(spreadSheet)
spreadColumns = columns + 1

totalRow = []
for column in range(spreadColumns):
    columnTotal = 0
    for i in range(rows):
        columnTotal += spreadSheet[i][column]
    totalRow.append(columnTotal)
spreadSheet.append(totalRow)
# print(spreadSheet)

for spreadRow in spreadSheet:
    row_str = [str(element) for element in spreadRow]
    print(' '.join(row_str))

