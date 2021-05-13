# 136 A

a, b, c = map(int, input().split())

if c >= (a-b):  
    print(c - (a-b))
elif c < (a-b):
    print(0)