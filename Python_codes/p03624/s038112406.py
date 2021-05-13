S = input()
l = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(l)):
    if l[i] not in S:
        print(l[i])
        exit(0)
else:
    print('None')