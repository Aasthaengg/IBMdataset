#coding:UTF-8

n = input()
a = []
for i in range(n):
        a = map(int,raw_input().split())
        a.sort()
        if(a[2]**2 == a[0]**2 + a[1]**2):
            print 'YES'
        else:
            print 'NO'