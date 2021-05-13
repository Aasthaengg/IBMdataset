a,b,x = map(int,input().split())
a_num = 0
b_num = 0
if a == 0:
    b_num = (b//x)+1
else:
    a_num = ((a-1)//x)+1
    b_num = (b//x)+1
print(b_num-a_num)