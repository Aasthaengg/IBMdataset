n = int(input())
a = map(int, input().split())

f = 0
o = 0
t = 0
for i in a:
    if i % 4 == 0:
        f += 1
    elif i % 2 == 0:
        t += 1
    else:
        o += 1
isok = True;
if t%2 == 1:
    f -= 1
if o > f+1:
    isok = False


print('Yes' if isok else 'No')
