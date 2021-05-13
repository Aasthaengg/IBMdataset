#C

s = list(input())
zero = 0
one = 0
for i in s:
    if i == "1":
        one += 1
    else:
        zero += 1
print(2*min(one, zero))
