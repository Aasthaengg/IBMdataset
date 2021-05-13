S = set(input())
s = list('abcdefghijklmnopqrstuvwxyz')
for i in s:
    if i not in S:
        print(i)
        exit()
print('None')