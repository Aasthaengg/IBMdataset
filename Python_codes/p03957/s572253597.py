# coding: utf-8

text = input().rstrip()
c_index = text.find("C")
f_index = text.find("F", c_index)

print("Yes" if (0 <= c_index < f_index and f_index >= 0) else "No")
