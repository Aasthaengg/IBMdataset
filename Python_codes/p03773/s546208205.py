#Remaining Time
A, B = map(int,input().split())
begin = A + B
if begin >= 24:
    begin = begin - 24
print(begin)