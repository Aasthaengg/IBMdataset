import sys
r,c = map(int,raw_input().split())
col_sum=[0]*c
for  i in range(r):
    row=map(int,raw_input().split())
    row.append(sum(row))
    for j in range (c):
        col_sum[j] += row[j]
    print ' '.join(map(str,row))
for i in range(c):
    print col_sum[i],
print sum(col_sum)