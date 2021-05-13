# coding: utf-8

num = int(input())
ok = 0
for i in range(1, 10):
    for j in range(1, 10):
        if num == i * j:
            print("Yes")
            ok += 1
            exit()
if ok == 0:
    print("No")