# coding: utf-8
# Your code here!

S = input()

# print(S)

# print(len(S))

if len(S) == 2:
    print(S)
elif len(S) == 3:
    s_reversed = reversed(S)
    # print(s_reversed)
    # print(S.reverse())
    print(S[::-1])
else:
    pass
