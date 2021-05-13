s = input()

data = ["A", "C", "G", "T"]

max_ = 0
tmp = 0
for i in range( len(s) ):
    if s[i] in data:
        tmp += 1
        if tmp >= max_:
            max_ = tmp
    else:
        tmp = 0

print(max_)
