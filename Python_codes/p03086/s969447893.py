import sys
S = list(input())
X = ["A","C","G","T"]

max_len = 0
cur = 0

for i in S:
    if i in X: cur += 1
    else:
        if cur> max_len:
            max_len = 0
            max_len +=cur
            cur = 0
        else:
            cur = 0

if cur > max_len:
    print(cur)
    sys.exit()

print(max_len)