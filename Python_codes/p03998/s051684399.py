a = list(input())
b = list(input())
c = list(input())

i = 1
j = 0
k = 0
last = a[0]

while i<=len(a) and j<=len(b) and k<=len(c):
    if last == 'a':
        if i < len(a):
            last = a[i]
        i += 1
    if last == 'b':
        if j < len(b):
            last = b[j]
        j += 1
    if last == 'c':
        if k < len(c):
            last = c[k]
        k += 1

if i == len(a)+1:
    print('A')
elif j == len(b)+1:
    print('B')
elif k == len(c)+1:
    print('C')