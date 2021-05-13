n = list(input())

if len(n) == 1:
    print(n[0])
elif n[0] == '1':
    if n.count('9') == len(n) - 1:
        print(1 + 9 * (len(n) - 1))
    else:
        print(9 * (len(n) - 1))
elif n.count('9') == len(n):
    print(9 * len(n))
elif n.count('9') == len(n) - 1:
    if n[0] != '9':
        print((int(n[0])) + (9 * (len(n) - 1)))
    else:
        print(9 * (len(n) - 1) + 8)
else:
    print((int(n[0]) - 1 ) + (9 * (len(n) - 1))) 