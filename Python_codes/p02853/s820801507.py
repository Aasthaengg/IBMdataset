X,Y=map(int,input().split())

sum_=0
if 1<=X<=3:
    sum_+=100000*(4-X)
if 1<=Y<=3:
    sum_+=100000*(4-Y)
if X == 1 and Y ==1:
    sum_+=400000

print(sum_)