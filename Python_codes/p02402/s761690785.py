#coding:utf-8
#1_4_D 2015.3.29
n = input()
data = list(map(int,input().split()))
sum = 0
for elem in data:
    sum += elem
print('{} {} {}'.format(min(data),max(data),sum))