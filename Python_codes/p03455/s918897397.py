# 1<=a,b<=10000
# a,bは整数

#number = input('整数を入力してね > ')
#print (number)
a, b = map(int, input().split())
#print(a, b)
c = a * b
#print(c)
d=c%2
if d==0:
    print('Even')
if d==1:
    print('Odd')