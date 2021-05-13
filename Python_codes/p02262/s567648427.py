# -*- coding:utf-8 -*-

cnt = 0
def insection_sort(a, g):
    global cnt
    for i in range(g, len(a)):
        v = a[i]
        j = i - g
        while j >= 0 and a[j] > v:
            a[j+g] = a[j]
            j -= g
            cnt += 1
        a[j+g] = v

def shell_sort(a):
    g = [1]
    temp = 4
    while temp < len(a):
        g.append(temp)
        temp = 3 * temp + 1

    print(len(g))
    for youso in reversed(g):
        if youso != 1:
            print(youso, end=' ')
        else:
            print(youso)
        insection_sort(a, youso)

inp_num = int(input())
a = list()
for i in range(inp_num):
    a.append(int(input()))
shell_sort(a)
print(cnt)
for i in a:
    print(i)