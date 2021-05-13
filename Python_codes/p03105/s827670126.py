i = input().split()

i = list(map(int, i))

if i[0] * i[2] < i[1]:
    print(i[2])
else:
    print(int(i[1]/i[0]))