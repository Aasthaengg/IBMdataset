import sys
h,w = map(int, input().split())
s = [[''] * w] * h
for i in range(h):
    s[i] = list(str(input()))

# '#'が縦横にあったらfalse
def sirokuro(i,j):
    result = True
    if i + 1  < h :
        if s[i + 1][j] == '#':
            result = False
    if i - 1 >= 0:
        if s[i - 1][j] == '#':
            result = False
    if j + 1 < w:

        if s[i][j + 1] == '#':

            result = False
    if j - 1 >= 0:
        if s[i][j - 1] == '#':
            result = False
    return result

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            if sirokuro(i,j):
                print('No')
                sys.exit()
print('Yes')