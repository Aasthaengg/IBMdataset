r,c = [int(x) for x in input().split()]
sheet =[[int(x) for x in input().split()] for y in range(r)]
col_sum = [0]*c
for i in sheet:
    print(" ".join(map(str,i))+" "+str(sum(i)))
    for j in range(c):
        col_sum[j] += i[j]

print(" ".join(map(str,col_sum))+" "+str(sum(col_sum)))