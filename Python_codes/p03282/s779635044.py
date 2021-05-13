s = input()
k = int(input())

for i, x in enumerate(s):
    if x == '1':
        if k == i + 1:
            print(1)
            exit()
    else:
        print(x)
        exit() 