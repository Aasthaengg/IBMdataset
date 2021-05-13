#coding:utf-8

n = int(input().rstrip())

sl = [i for i in range(1,14)]
hl = [i for i in range(1,14)]
cl = [i for i in range(1,14)]
dl = [i for i in range(1,14)]

for i in range(n):
    mark, rank = input().rstrip().split(" ")
    rank = int(rank)

    if mark == "S":
        sl.remove(rank)
    elif mark =="H":
        hl.remove(rank)
    elif mark =="C":
        cl.remove(rank)
    else:
        dl.remove(rank)

#??????
"""
sl.reverse()
hl.reverse()
cl.reverse()
dl.reverse()
"""
for j in sl:
    print("S "+ str(j))
for j in hl:
    print("H "+ str(j))
for j in cl:
    print("C "+ str(j))
for j in dl:
    print("D "+ str(j))