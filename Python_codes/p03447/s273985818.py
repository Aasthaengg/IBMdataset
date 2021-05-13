lst = []
for _ in range(3):
    lst.append(int(input()))
print((lst[0]-lst[1]) % lst[2])