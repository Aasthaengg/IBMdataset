r,c = [int(x) for x in input().split()]
s_row = [0 for x in range(c+1)]
for i in range(r):
    row = [int(x) for x in input().split()]
    row.append(sum(row))
    print(" ".join([str(x) for x in row]))
    s_row = [x+y for x,y in zip(s_row,row)]
print(" ".join([str(x) for x in s_row]))
