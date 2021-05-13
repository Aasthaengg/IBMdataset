S = input()
S = S[::-1]
a = 'dream'[::-1]
b = 'dreamer'[::-1]
c = 'erase'[::-1]
d = 'eraser'[::-1]
words = [a, b, c, d]
t = 0
for i in range(1, len(S) + 1):
    if S[t:i] in words:
        t = i
if t == len(S):
    print('YES')
else:
    print('NO')
