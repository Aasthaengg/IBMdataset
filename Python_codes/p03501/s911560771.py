num = input().split()
i = [int(s) for s in num]

if(i[0]*i[1] > i[2]):
    print(i[2])
else:
    print(i[0]*i[1])