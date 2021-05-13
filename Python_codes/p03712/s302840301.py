# -*- coding: utf-8 -*-
H, W = map(int, input().split())
print("#"*(W+2))
for i in range(H):
    text = "#"
    text += input()
    text += "#"
    print(text)
print("#"*(W+2))
