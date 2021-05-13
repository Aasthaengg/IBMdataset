n = int(input())
s = input()
c = 0
maxc = 0
for i in s:
    if i == 'I':
        c += 1
    else:
        c -= 1
    if maxc < c:
        maxc = c
print(maxc)