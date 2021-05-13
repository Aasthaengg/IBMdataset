s = list(input())
l = []
for i,j in enumerate(s):
    if i%2==0:
        l.append(j)
print(''.join(l))