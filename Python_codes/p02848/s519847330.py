n = int(input())
s = input()
t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(''.join([t[t.index(c) + n] for c in s ]))