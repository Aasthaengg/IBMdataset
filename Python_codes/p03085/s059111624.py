bases = [{'A', 'T'}, {'C', 'G'}]
b = input()
for i in bases:
    if b in i:
        print((i - set(b)).pop())