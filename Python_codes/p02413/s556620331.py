#coding:utf-8
#1_7_C 2015.4.6
r,c = map(int,input().split())
sheet = [list(map(int,input().split())) for i in range(r)]

for row in sheet:
    row.append(sum(row))

s = [sum(list(row[i] for row in sheet)) for i in range(c + 1)]
sheet.append(s)

for row in sheet:
    print(*row)