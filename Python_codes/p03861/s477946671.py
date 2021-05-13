import math
a,b,x = map(int,input().split())
b_ans = b//x
a_ans = a//x
a_amari = a%x
print(b_ans-(a_ans+(a_amari>0))+1)