# coding: utf-8
# Your code here!
w, a, b = map(int,input().split())
if a < b:
    if a <= b <= a + w:
        print(0)
    else:
        print(abs(a+w-b))
    
else:
    if b <= a <= b + w:
        print(0)
    else:
        print(abs(b+w-a))