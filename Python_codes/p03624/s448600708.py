S = set(input())
for i in range(97, 123):
    c = chr(i)
    if c not in S:
        print(c)
        exit()
print('None')