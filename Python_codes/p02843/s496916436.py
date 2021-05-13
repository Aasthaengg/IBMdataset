# -*- coding: utf-8 -*-

X = int(input())

num = X // 100
reminder = X % 100
if reminder == 0:
    print("1")
    exit()

for i in range(num+1):
    for j in range(num+1):
        if i+j > num:
            continue
        for k in range(num+1):
            if i+j+k > num:
                continue
            for l in range(num+1):
                if i+j+k+l>num:
                    continue
                for m in range(num+1):
                    if i+j+k+l+m>num:
                        continue

                    res = i*1+j*2+k*3+l*4+m*5
                    if res == reminder:
                        print("1")
                        exit()

print("0")
