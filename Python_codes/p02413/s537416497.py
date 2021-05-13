# coding: UTF-8
r,c = map(int,raw_input().split(" "))
mtrix = [map(int,raw_input().split()) for i in range(r)]
last_line = [0 for i in range(c+1)]
for i in range(r):
    mtrix[i].append(sum(mtrix[i]))
    last_line = [x+y for (x,y) in zip(mtrix[i],last_line)]
mtrix.extend([last_line])
for i in range(r+1):
    print " ".join(map(str,mtrix[i]))


