#coding:utf-8

w = input().rstrip()

bun =[]
a =""
while a !="END_OF_TEXT":
    a = input().rstrip()
    if a =="END_OF_TEXT":
        break

    bun += a.lower().split()

print(bun.count(w))