s = list(input())
s = set(s)
m = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(m)):
    if not m[i] in s:
        print(m[i])
        exit(0)
print('None')