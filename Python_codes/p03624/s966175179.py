a = "abcdefghijklmnopqrstuvwxyz"
S = str(input())
l = []

for i in range(26):
    if not a[i] in S:
        l.append(i)

if not l:
    print('None')

else:
    print(a[min(l)])