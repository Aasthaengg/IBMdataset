#coding:utf-8

abc = raw_input().split()

a = int(abc[0])
b = int(abc[1])
c = int(abc[2])

cnt = 0

for i in range(a, b+1):
    if c % i == 0:
        cnt += 1

print cnt