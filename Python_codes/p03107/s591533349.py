ss = input()
zero = 0
one = 0
for s in ss:
    if s == "0":
        zero += 1
    elif s == "1":
        one += 1
print(2 * min(zero, one))