s = input()
w = int(input())

len_ = 0
if len(s) % w == 0:
    len_ = len(s)//w
else:
    len_ = len(s) // w + 1
for i in range(len_):
    print(s[w*i], end="")
print()