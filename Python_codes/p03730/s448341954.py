# coding: utf-8

a, b, c = map(int, input().split(" "))

if 1 <= len(list(filter(lambda x: x == c, map(lambda x: x % b, range(a, a*b, a))))):
    print("YES")
else:
    print("NO")




