d = {}
n = int(input())
for _ in range(n):
    a, b = input().split()
    if a == 'insert':
        d[b] = b
    elif a == 'find':
        print('yes' if b in d.keys() else 'no')
