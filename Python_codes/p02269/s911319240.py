n = int(input())
d = set()
for i in range(n):
    cmd, val = input().split()
    if cmd == 'insert':
        d.add(val)
    else:
        print('yes'*(val in d)or'no')