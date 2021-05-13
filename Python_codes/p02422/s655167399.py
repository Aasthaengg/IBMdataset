#coding:utf-8
#1_9_D 2015.4.13
s = list(input())
n = int(input())
for i in range(n):
    c = input().split()
    if c[0] == 'print':
        print(''.join(s[int(c[1]) : int(c[2])+1]))
    elif c[0] == 'reverse' and c[1] != '0':
        s[int(c[1]) : int(c[2])+1] = s[int(c[2]) : int(c[1])-1 :-1]
    elif c[0] == 'reverse' and c[1] == '0':
        s[:int(c[2])+1] = s[int(c[2])::-1]
    else: #replace
        s[int(c[1]) : int(c[2])+1] = list(c[3])